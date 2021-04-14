# I have created this file - Gopi Jaiswal
from django.http import HttpResponse 
from django.shortcuts import render
#def index(request): # if request is not given it will through an error 
#    return HttpResponse(''' <h1> Hello Gopi Jaiswal </h1> <a href="https://www.geeksforgeeks.org/">GeeksForgeeks </a>''')
#def about(request):
#    return HttpResponse("About Gopi Jaiswal")

def index(request): # if request is not given it will through an error 
    return render(request,'index.html')
  #  return HttpResponse("<h1>Home</h1>")


def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    removepuch=request.GET.get('removepunc','off') # make default = off
    print(removepuch)
    print(djtext)
    # analyze the text
    analyzed= ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepuch == "on":

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    #return HttpResponse("remove puncuation")
    else:
        return HttpResponse("Error")
'''def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove(request):
    return HttpResponse("space remover " "<a href='/'>back</a>")

def charcounter(request):
    return HttpResponse("character counter")
'''