from django.shortcuts import render

def homepage(request):
    return render(request, "public/homepage.html")

def wypowiedzi(request):
    return render(request, "public/wypowiedzi.html")
