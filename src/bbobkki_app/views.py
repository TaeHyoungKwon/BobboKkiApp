from django.shortcuts import render

def index(request):
    return render(request,"bbobkki_app/index.html",{})
