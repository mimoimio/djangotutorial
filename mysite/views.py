from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the / index. lol")
    
def about(request):
    return render(request, "about.html")