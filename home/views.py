from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>this is the https response on main page</h1>
    <hr>
    <h3>by - rugved vangari</h3>
""")


def success(request):
    return HttpResponse("""
    <h1>This is the success page</h1>
    <p style= "color:red">running in success router<p>
""")

def another(request):
    return HttpResponse("<h2> Hi! Rugved Vangari here!</h2>")

def render_req(request):

    peoples = [
        {'name':'rugved','age' : 17}, {'name':'rehan','age': 18}, {'name': 'piyush','age': 18}, {'name':'aditya','age': 19}
    ]

    vages = [
        'potato', 'tomato', 'cucumber', 'methi', 'mango', 'sabji'
    ]

    text = "this is rugved vangari learning the django ! and wna tto get internship in s.y."

    for people in peoples:
        print(people)

    home = "Home page"

    return render(request, "home_app/index.html", context= {'peoples':peoples, 'text' : text, 'vages' : vages, 'page' : home})

def about(request):

    ab = "About page"
    return render(request, "home_app/about.html", context = {'page' : ab})

def help(request):
    hlp = "helping page" 
    return render(request, "home_app/help.html", context = {'page' : hlp})