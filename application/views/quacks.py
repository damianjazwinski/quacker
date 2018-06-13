from django.shortcuts import render, redirect
from application.models import Quack, OptionalMention
from application.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def quack(request):
	if request.method == "POST":
		quack = Quack()
		quack.content = request.POST['quack-content']
		quack.quacker = request.user
		quack.save()

		parsed = ( t for t in quack.content.split() if t.startswith('@') )
		for nick in parsed:
			fixed = nick[1:]
			if fixed == request.user.username:
				continue
			try:
				mention = User.objects.get(username=fixed)
				opt = OptionalMention()
				opt.mention = mention
				opt.quack = quack
				opt.save()
			except User.DoesNotExist:
				pass


	return redirect('index')