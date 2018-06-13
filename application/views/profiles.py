from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from application.models import Quack, Follow, Profile
from django.contrib.auth.decorators import login_required
from application.forms import UserPanelForm

def profile(request, username):
	context ={}
	try:
		user = User.objects.get(username=username)
		profile = Profile.objects.get(user=user)
		context.update({
			'myprofile': profile,
		})
		
		if request.user.is_authenticated:
			follower = request.user

			if request.method == "POST":
				try:
					follow = Follow.objects.get(follower=follower, followed=user)
					follow.delete()
				except Follow.DoesNotExist:
					start_following = Follow()
					start_following.follower = follower
					start_following.followed = user
					start_following.save()

			if len(Follow.objects.filter(follower=follower, followed=user)):
				context.update({
					'is_following': True
				})
		context.update(get_user_context(user))
	except User.DoesNotExist:
		return render(request, 'profiles/profile.html', {})

	return render(request, 'profiles/profile.html', context)

@login_required(login_url='/login/')
def userpanel(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == "POST":
		form = UserPanelForm(request.POST)
		if form.is_valid():
			if request.POST['image_link']:
				profile.image_link = request.POST['image_link']
			if request.POST['description']:
				profile.description = request.POST['description']
			profile.save()
			return redirect('/profile/' + request.user.username)
	else:
		form = UserPanelForm()
	print(profile.image_link)
	context = {
		'form': form,
		'myprofile': profile,
	}
	context.update(get_user_context(request.user))
	return render(request, 'profiles/userpanel.html', context)

@login_required(login_url='/login/')
def follows(request):
	if request.method == "POST":
		follow_to_delete = Follow.objects.get(pk=request.POST['id'])
		follow_to_delete.delete()

	context = get_user_context(request.user)
	followed_list = Follow.objects.filter(follower=request.user)
	follower_list = Follow.objects.filter(followed=request.user)
	followed_imgs = []
	follower_imgs = []
	for item in followed_list:
		followed_imgs.append({
			'profile': item,
			'link': Profile.objects.get(user=item.followed).image_link
		})
	for item in follower_list:
		follower_imgs.append({
			'profile': item,
			'link': Profile.objects.get(user=item.follower).image_link
		})
		print(Profile.objects.get(user=item.follower).image_link)
	context.update({
		'followed_imgs': followed_imgs,
		'follower_imgs': follower_imgs,
		'myprofile': Profile.objects.get(user=request.user)
	})

	return render(request, 'profiles/follows.html', context)

def get_user_context(user):
	quacks = sorted(Quack.objects.filter(quacker=user), key=lambda quack: quack.created_at, reverse=True)
	return {
		'profile': user,
		'quacks': len(quacks),
		'following': len(Follow.objects.filter(follower=user)),
		'followers': len(Follow.objects.filter(followed=user)),
		'quack_list': quacks,
	}