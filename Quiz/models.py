from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

