from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    context = {
        'form': UserCreationForm()
    }
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            auth.login(request, user)
            return redirect('index')
        else:
            context['form'] = form

    return render(request, 'registration/signup.html', context)
