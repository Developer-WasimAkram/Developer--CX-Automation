from django.shortcuts import render,redirect

# Create your views here.

def user_login(request):
    
    if request.method == 'POST':
        # code for user authentication
        # if authentication successful
        return redirect('home')
   
    return render(request, 'accounts/login.html')