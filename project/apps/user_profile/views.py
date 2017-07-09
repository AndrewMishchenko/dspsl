from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserCreationForm()
    return render(request, 'user_profile/signup.html', {'form': form})


def login(request):
    if request.method == 'POST' and request.is_ajax():
        print 'ajax'
        print request.POST
        data = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (not user is None) and (user.is_active):
            auth_login(request, user)
            if not request.POST.get('rem', None):
                request.session.set_expiry(0)
            data['status'] = 'true'  # "You have been successfully Logged In"
            data['userr'] = user.profile.id
        else:
            data['status'] = 'false'  # "There was an error logging you in. Please Try again"
    return JsonResponse(data)
