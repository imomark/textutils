from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    analyzedText = request.POST.get('text')
    removepunc = request.POST.get('removepunc','off')
    newremove = request.POST.get('newremove','off')
    charcount = request.POST.get('charcount','off')
    spaceremove = request.POST.get('spaceremove','off')
    upper = request.POST.get('upper','off')
    lower = request.POST.get('lower','off')
    Error = True
    count = 0
    if removepunc == 'on':
        analyzedText= removePunc(analyzedText)
        print('i was here ')
        print(analyzedText)
        Error = False
    if newremove == 'on':
        analyzedText= newLineremover(analyzedText)
        Error = False
    if charcount == 'on':
        count = charCount(analyzedText)
        Error = False
    if spaceremove == 'on':
        analyzedText = extraSpaceRemover(analyzedText)
        Error = False
    if upper == 'on':
        analyzedText = analyzedText.upper()
        Error = False
    if lower == 'on':
        analyzedText = analyzedText.lower()
        Error = False
    if Error:
        analyzedText = 'Error'
    if count != 0:
        params = {'analyzedText': analyzedText,'count':"The character count is [{}]".format(count)}
    else:
        params = {'analyzedText': analyzedText}
    return render(request, 'analyze.html',params)

def removePunc(value):
    analyzedText=""
    punc = '''.,!?:;“”‘’()''{}[]@*~/–#$&'''
    for char in value:
        if char not in punc:
            analyzedText = analyzedText + char
    return analyzedText

def newLineremover(value):
    analyzedText=""
    for char in value:
        if not(char == "\n" or char=="\r"):
            analyzedText = analyzedText + char
    return analyzedText

def charCount(value):
    count = 0
    for char in value:
        if not(char == " " or char == "\n" or char == "\r"):
            count =  count + 1
    return count

def extraSpaceRemover(value):
    analyzedText = ""
    for index ,char in enumerate(value):
        if not(value[index]==" " and value[index + 1] == " "):
            analyzedText = analyzedText + char
    return analyzedText


        


