from django.shortcuts import render, HttpResponse
from .models import FlashWord

from django.shortcuts import render
from .models import FlashWord

def flash_word(request):
    if request.method == 'GET':
        flash_words = FlashWord.objects.order_by('?')[:1]  # Retrieve 1 random flash word

        context = {
            'flash_word': flash_words[0],
            'show_full_word': False,
        }

        return render(request, 'flash_word.html', context)

    elif request.method == 'POST':
        flash_words = FlashWord.objects.order_by('?')[:1]  # Retrieve 1 random flash word

        context = {
            'flash_word': flash_words[0],
            'show_full_word': True,
        }

        return render(request, 'flash_word.html', context)


def home(request):
    return render(request,'index.html')
