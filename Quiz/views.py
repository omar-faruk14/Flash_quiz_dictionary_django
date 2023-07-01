from django.shortcuts import render, redirect, HttpResponse
from .models import Quiz, Question, Choice
from django.views.decorators.http import require_POST
from django.contrib import messages


def create_quiz(request):
    if request.method == 'POST':
        # Retrieve form data
        quiz_title = request.POST['quiz_title']
        question_text = request.POST['question_text']
        choices = request.POST.getlist('choices')
        correct_choice = int(request.POST['correct_choice'])

        # Create Quiz instance
        quiz = Quiz.objects.create(title=quiz_title)

        # Create Question instance associated with the Quiz
        question = Question.objects.create(quiz=quiz, text=question_text)

        # Create Choices associated with the Question
        for i, choice_text in enumerate(choices):
            is_correct = (i == correct_choice)
            Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)

        return redirect('quiz-list')
    else:
        return render(request, 'quiz/create_quiz.html')

def create_quiz_with_option(request):
    if request.method == 'POST':
        # Retrieve form data
        quiz_id = request.POST['quiz_title']
        question_text = request.POST['question_text']
        choices = request.POST.getlist('choices')
        correct_choice = int(request.POST['correct_choice'])

        # Create Question instance associated with the Quiz
        question = Question.objects.create(quiz_id=quiz_id, text=question_text)

        # Create Choices associated with the Question
        for i, choice_text in enumerate(choices):
            is_correct = (i == correct_choice)
            Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)

        return redirect('quiz-list')
    else:
        quizzes = Quiz.objects.all()
        return render(request, 'quiz/create_quiz_option.html', {'quizzes': quizzes})




def start_quiz(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes
    }
    return render(request, 'quiz/start_quiz.html', context)

def quiz_page(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()
    context = {
        'quiz': quiz,
        'questions': questions
    }
    return render(request, 'quiz/quiz_page.html', context)

@require_POST
def submit_quiz(request):
    quiz_id = request.POST.get('quiz_id')
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()

    score = 0
    total_questions = 0

    for question in questions:
        choice_ids = request.POST.getlist(f'choice{question.id}')
        selected_choices = Choice.objects.filter(id__in=choice_ids)
        correct_choices = question.choice_set.filter(is_correct=True)

        if set(selected_choices) == set(correct_choices):
            score += 1

        total_questions += 1

    # Pass the score and total questions as context variables
    return redirect('result_page', score=score, total_questions=total_questions)

def result_page(request, score, total_questions):
    return render(request, 'quiz/submit_quiz.html', {'score': score, 'total_questions': total_questions})



