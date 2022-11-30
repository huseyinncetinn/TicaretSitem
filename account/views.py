
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def login_request (request):
    if request.method == 'POST':       
        if 'login' in request.POST:          
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate (request , username = username , password = password)
            if user is not None :
                login(request , user)
                return redirect('Alibaba')
            else:
                return render (request , 'login.html' , {
                    'error' : 'username ya da password yalnış'
                })
        
    return render (request , 'login.html')

def register_request (request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username =username).exists():
                return render(request , 'register.html' , 
                {   
                    'error':'Username kullanılıyor',
                    'username' : username,
                    'email' : email,
                    'firstname' : firstname,
                    'lastname' : lastname
                })
            else : 
                if User.objects.filter(email = email).exists():
                   return render(request , 'register.html' , 
                   {
                        'error':'Email kullanılıyor',
                        'username' : username,
                        'email' : email,
                        'firstname' : firstname,
                        'lastname' : lastname
                   })
                else:
                    user =User.objects.create_user(username = username , email = email , first_name =firstname , last_name = lastname , password = password)
                    user.save()
                    return redirect('Alibaba')
                    

        else:
            return render(request , 'register.html' , 
            {
                    'error':'Parola eşleşmiyor',
                    'username' : username,
                    'email' : email,
                    'firstname' : firstname,
                    'lastname' : lastname
            })


    return render (request , 'register.html')

def logout_request (request):
    logout(request)
    return redirect ('Alibaba')
