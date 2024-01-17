# Created by Yashasvika
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    details = {'name': 'Yashi', 'age': 20}
    return render(request, 'index.html', details)
    # return HttpResponse("hello from index")

def analyzer (request):
    textEntered = request.POST.get("text", "default text")
    rempunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    spaceremover = request.POST.get("spaceremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charcounter = request.POST.get("charcounter", "off")
    # here "text" is the name that we gave to the textarea in our html code
    # and "default text" is the text that will be printed if textbox is empty.

    if rempunc == "on":
        punctuations = '''!@#$%^&*()-_+=[]{}|;:'",.<>/?'''
        analyzed = ""
        for char in textEntered:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if fullcaps == "on":
        analyzed = ""
        for char in textEntered:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Uppercase Text", "analyzed_text": analyzed}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if newlineremover == "on":
        analyzed = ""
        for char in textEntered:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "No new Line", "analyzed_text": analyzed}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if spaceremover == "on":
        analyzed = ""
        for char in textEntered:
            if char != " ":
                analyzed = analyzed + char
        params = {"purpose": "No Space", "analyzed_text": analyzed}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if extraspaceremover == "on":
        analyzed = ""
        # Ennumerate function fetches the character as well as index of that character
        for index, char in enumerate(textEntered):
            if textEntered[index] == " " and textEntered[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {"purpose": "Extra Space Removed", "analyzed_text": analyzed}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if charcounter == "on":
        msg = ""
        counter = 0
        for char in textEntered:
            counter = counter + 1
            msg = "Number of characters are " + str(counter)
        params = {"purpose": "Extra Space Removed", "analyzed_text": msg}
        textEntered = analyzed
        # return render(request, "analyze.html", params)
    if (charcounter != "on" and extraspaceremover != "on" and spaceremover != "on" and newlineremover != "on" and fullcaps != "on" and rempunc != "on"):
        return HttpResponse("Please Select your option.")

    return render(request, "analyze.html", params)

def new(request):
    return HttpResponse('''<h1>Yashi</h1> <a href="https://www.netflix.com/browse">Netflix</a>''')