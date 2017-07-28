from django.shortcuts import render, redirect, HttpResponse
# from models import User
from django.contrib import messages
from .. login_app.models import User
from models import Poke

def index(request):
	if not request.session['id']:
		return redirect('/')
	context = {
	"users": User.objects.exclude(id = request.session['id']),
	"this_user": User.objects.filter(id = request.session['id']),
	"my_pokeCount": Poke.objects.filter(receiver = request.session['id']).count(),
	"mypokes": Poke.objects.filter(receiver = request.session['id']),
	"pokes": Poke.objects.all()
	}
	return render(request, 'pokes_app/index.html', context)

def logout(request):
	request.session['id'] = None
	return redirect('/loggedOut')

def givePoke(request, id):
	pokeGiver = User.objects.get(id = request.session['id'])
	pokeGetter = User.objects.get(id = request.POST['receiver'])
	pokeGiven = Poke.objects.create(giver = pokeGiver, receiver = pokeGetter)
	get_poked_count = Poke.objects.all().count()
	print pokeGiver.name, pokeGetter.name
	return redirect('/pokes')	



