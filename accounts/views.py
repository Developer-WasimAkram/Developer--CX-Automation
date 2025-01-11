from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html' ,{'error': 'Invalid Credential Authentication failed'} )
        # code for user authentication
        # if authentication successful
    return render(request, 'accounts/login.html' )


def user_signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        if  not User.objects.filter(username=username).exists() and(password1==password2):
            # code for user registration
            # if registration successful
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
            user.save()
            return redirect('login')  
        elif User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
    return render(request, 'accounts/signup.html' )

#@login_required
def dashboard(request):
    
    return render(request, 'home/AppPage.html')

def log_out(request):
    # code for user logout
    logout(request)
    return redirect('login')