from django.shortcuts import render, HttpResponse
from .models import FlashWord
import random

def flashcard_view(request):
    # Get a random word from the database
    random_word = FlashWord.objects.order_by('?').first()

    context = {
        'word': random_word
    }
    return render(request, 'flashcards.html', context)


def home(request):
    return render(request,'index.html')
