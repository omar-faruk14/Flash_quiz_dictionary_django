from django import forms
from .models import Quiz, Question, Choice

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text']
        widgets = {
            'quiz': forms.Select(attrs={'class': 'form-select'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'is_correct']
        widgets = {
            'question': forms.Select(attrs={'class': 'form-select'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
