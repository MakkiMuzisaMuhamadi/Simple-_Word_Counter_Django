from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request, 'index.html')



def counter(request):
    words = request.POST['text']
    amount = len(words.split())
    return render(request, 'amount.html', {'amount_of_words': amount})


