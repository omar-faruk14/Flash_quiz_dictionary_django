from django.db import models

class FlashWord(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    example = models.TextField()
    kanji = models.CharField(max_length=100)

    def __str__(self):
        return self.word
