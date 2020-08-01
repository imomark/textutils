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
