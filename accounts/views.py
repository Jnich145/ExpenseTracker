from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User

# Still working on this
def login_view(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")
    
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:

                user = User.objects.create_user(
                    username=username,
                    password=password
                    )
                
                login(request, user)

                return redirect('home')
            else:
                form.add_error('password_confirmation', 'The passwords do not match.') 
    else:
        form = SignUpForm()
        context = {
            "form": form
        }

    return render(request, 'accounts/signup.html', context)    
