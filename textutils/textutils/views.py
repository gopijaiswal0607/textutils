# I have created this file - Gopi Jaiswal
from django.http import HttpResponse 
from django.shortcuts import render
#def index(request): # if request is not given it will through an error 
#    return HttpResponse(''' <h1> Hello Gopi Jaiswal </h1> <a href="https://www.geeksforgeeks.org/">GeeksForgeeks </a>''')
#def about(request):
#    return HttpResponse("About Gopi Jaiswal")

def index(request): # if request is not given it will through an error 
    params={'name':'Gopi','place':'Mars'}
    return render(request,'index.html',params)
  #  return HttpResponse("<h1>Home</h1>")
def removepunc(request):
    return HttpResponse("remove puncuation")
def capfirst(request):
    return HttpResponse("Capitalize first")
def newlineremove(request):
    return HttpResponse("New line remove")
def spaceremove(request):
    return HttpResponse("space remover " "<a href='/'>back</a>")
def charcounter(request):
    return HttpResponse("character counter")