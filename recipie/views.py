from django.shortcuts import render, redirect, get_object_or_404
from recipie.models import Recipies
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def recipies(request):
    if request.method == 'POST': #accepting the data by POST method from Html page (recipie.html)
        data = request.POST

        name_r = data.get("name_r") #getting recipie name
        dis_r = data.get("dis_r") #getting discription of recipie
        image = request.FILES.get("image") #getting the image of recipie

        print(name_r)
        print(dis_r)
        print(image)

        Recipies.objects.create(    #from models.py getting class objects (RECIPIES) and defining them by accepted 
                                    #variables
        name_r = name_r,
        dis_r = dis_r,
        image = image,
        )

        return redirect("/recipie/")  #return on same page

    query_set = Recipies.objects.all()  #for showcasing the objects
    context = {'recipies' : query_set} #adding the recipies in context to print on webpage (in table)
    
    return render(request, 'recipee.html', context)  

def delete(request, id):
    
    query_set = Recipies.objects.get(id = id)  #deleting the recipie if we want getting the id of it
    query_set.delete() #delete the recipie from its id
    return redirect('/recipie/') #redirecting to same page

def update(request, id):

    #get_object_or_404() is a shortcut function in Django used to fetch an object from the database. 
    #If the object does not exist, it automatically raises a 404 Not Found error instead of crashing the app.
    recipie = get_object_or_404(Recipies, id = id)  #getting the recipie id fro the table of which we want to update it
    context = {'recipie' : recipie} 

    if request.method == "POST":
        data = request.POST

        name_r = data.get("name_r")
        dis_r = data.get("dis_r")
        image = request.FILES.get("image")

        recipie.name_r = name_r   #updating recipie name
        recipie.dis_r = dis_r   #updating recipie discription

        if image :
            recipie.image = image    #updating the recipie image
        recipie.save()    #saving all the updated details
        return redirect('/recipie/')  #redirecting to the recipie page

    return render(request, 'update.html', context)

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):

    if request.method == "POST":     
        print("POST data:", request.POST)
        f_name = request.POST.get("f_name")   #getting first name
        l_name = request.POST.get("l_name") #getting last name
        username = request.POST.get("username")   #getting user name
        password = request.POST.get("passcode") #getting password

        if not username:  #if username is not entered
            return render(request, 'register.html', {'error': "Username is required."})  #show message
    
        user = User.objects.filter(username=username)       #serach if username entered is existed or not
        if user.exists():
            messages.info(request, "Username Already exist.") #yes - show the message
            return render(request, 'register.html')     

        user = User.objects.create_user(        
            first_name=f_name,  #setting the first name
            last_name=l_name,    #setting up the last name
            username=username,   #setting up the username
        )
    
        user.set_password(password)    #setting up the password
        user.save() #all the data is been saved in database

        messages.info(request, "Account Created successfully.")  #success message
        return redirect('/login/') #jump to login page

    return render(request, 'register.html')


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")   #getting username
        password = request.POST.get("passcode") #getting password

        if not username or not password:    #if no username or passsword entered
            messages.info(request, "Both fields are required.") #show message
            return redirect('/login/') #again jump to login page

        user = authenticate(username=username, password=password)   #if entered then check it is matching or not
        print("Authenticated user:", user)  # Debug line

        if user is not None:  #if entered all correct
            login(request, user)  #login the user
            return redirect('/recipie/') #jump to recipie page to add the recipie
        else:
            messages.info(request, "Invalid username or password.") #otherwise invalid passcode or username message
            return redirect('/login/') #again jump to login


    return render(request, 'login.html')

def logout_page(request):
    logout(request)  #button request to logout func.
    return redirect('/login/') #return back to login page
