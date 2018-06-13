from django.shortcuts import render, redirect
from application.models import Quack, Follow, OptionalMention, Profile
from itertools import chain

def index(request):
	context = {}
	if request.user.is_authenticated:
		my_follows = Follow.objects.filter(follower=request.user)
		all_quacks = Quack.objects.filter(quacker=request.user)
		mentions = OptionalMention.objects.filter(mention=request.user)
		
		#print('before: {0}', len(all_quacks))
		
		for follow in my_follows:
			follow_list = Quack.objects.filter(quacker=follow.followed)
			all_quacks = all_quacks | follow_list
		mentions_set = set()
		
		for mention in mentions:
			mentions_set.add(mention.quack.pk)

		all_quacks = sorted(all_quacks | Quack.objects.filter(pk__in=mentions_set), key=lambda quack: quack.created_at, reverse=True)
		context.update({
			'quacks': all_quacks,
			'myprofile': Profile.objects.get(user=request.user)
		})
		#print('after: {0}', len(all_quacks))

	return render(request, 'page/index.html', context)