from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    user_text = request.POST['text']
    words = len(user_text.split())
    vowelcount = 0
    consonantcount = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in user_text:
        if i in vowels:
            vowelcount += 1
        else:
            consonantcount += 1

    context = {
        'result_text' : user_text, 
        'wordcount' : words,
        'vowels' : vowelcount,
        'consonants' : consonantcount
    }
    return render(request, 'displayboard.html', context)