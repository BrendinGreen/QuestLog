from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

from Log.models import Objective
from Log.models import Game
from Log.models import Location
from Log.models import Skill
from django.contrib.auth.decorators import login_required


@login_required
def objectives(request):
    objs = Objective.objects.filter(user=request.user.id)
    return render(request, 'objective/index.html', {'objectives': objs})


@login_required
def games(request):
    games = Game.objects.filter(user=request.user.id)
    return render(request, 'game/index.html', {'games': games})


@login_required
def locations(request):
    locs = Location.objects.filter(user=request.user.id)
    return render(request, 'location/index.html', {'locations': locs})


@login_required
def skills(request):
    skills = Skill.objects.filter(user=request.user.id)
    return render(request, 'skill/index.html', {'skills': skills})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
