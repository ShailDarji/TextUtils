# I have created this file - Shail

from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # GET THE TEXT
    djtext = request.POST.get('text', 'default')

    # Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = string.punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if countchar == 'on':
        analyzed = 0
        for char in djtext:
            analyzed += 1

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}


    if removepunc != "on" and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and countchar != 'on':
        return HttpResponse("Error, Please Select Any Operation and try again")

    return render(request, 'analyze.html', params)
