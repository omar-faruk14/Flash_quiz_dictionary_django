from django.shortcuts import render, HttpResponse
from .models import FlashWord

def flash_word(request):
    flash_words = FlashWord.objects.order_by('?')[:1]  # Retrieve 5 random flash words

    context = {
        'flash_words': flash_words
    }

    return render(request, 'flash_word.html', context)

def home(request):
    return render(request,'index.html')
