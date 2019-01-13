from django.shortcuts import render, redirect
from django.urls import reverse
from login.forms import RegistrationForm


# Create your views here.
def login(request):
    return render(request, 'login/login.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index-home'))
        else:
            args = {'form': form}
            return render(request, 'login/signup.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'login/signup.html', args)