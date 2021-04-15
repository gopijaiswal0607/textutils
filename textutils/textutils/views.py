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
    capital= request.GET.get('capitalize','off')
    newlineremove = request.GET.get('newlineremover','off')
    extraspaceremove = request.GET.get('extraspaceremover','off')

    print(removepuch)
    print(djtext)
    # analyze the text
    analyzed= ""
    atext=djtext
    flag=0
    message=""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepuch == "on":
        message+='Removed Punctuations,'
        flag=1
        analyzed= ""
        for char in atext:
            if char not in punctuations:
                analyzed = analyzed+char
        atext=analyzed
        #params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
    #return HttpResponse("remove puncuation")
    if capital == 'on':
        message+='Capitalized form ,'
        flag=1
        analyzed= ""
        for char in atext:
            if char in punctuations:
                analyzed+=char
            else:
                analyzed+=char.upper()
        atext=analyzed
        #params={'purpose':'Capitalized form','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
    if newlineremove == 'on':
        flag=1
        message+= 'New line removed'
        analyzed=""
        for char in atext:
            if char != '\n':
                analyzed+= char
        atext = analyzed
    if extraspaceremove == 'on':
        flag=1
        message+= 'Extra space removed'
        analyzed = ""
        for char in atext:
            if char != ' ':
                analyzed+=char
        atext= analyzed 
    
    if flag==1:
        params={'purpose':message,'analyzed_text':atext}
        return render(request,'analyze.html',params)
    else:
        return render(request,'error.html')
        #return HttpResponse('<h1>Error!!! You have not checked any options </h1>')
'''def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove(request):
    return HttpResponse("space remover " "<a href='/'>back</a>")

def charcounter(request):
    return HttpResponse("character counter")
'''