from django.shortcuts import render, redirect
from .models import Quiz, Question, Choice

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
    if request.method == 'POST':
        # Assuming you have a form to start the quiz
        quiz_id = request.POST.get('quiz_id')
        # Retrieve the first question
        first_question = Question.objects.filter(quiz_id=quiz_id).first()
        if first_question:
            return redirect('question_page', question_id=first_question.id)
        else:
            # Handle the case where no questions are found for the quiz
            pass
    else:
        quizzes = Quiz.objects.all()
        return render(request, 'quiz/start_quiz.html', {'quizzes': quizzes})

def question_page(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = Choice.objects.get(id=selected_choice_id)
        # Perform any necessary calculations or checks for correctness
        # Store the user's response or perform any required actions

        # Get the next question
        next_question = Question.objects.filter(id__gt=question.id).first()
        if next_question:
            return redirect('question_page', question_id=next_question.id)
        else:
            return redirect('quiz_result')
    else:
        return render(request, 'quiz/question_page.html', {'question': question, 'choices': choices})

def quiz_result(request):
    # Perform any necessary calculations or checks for the final result
    return render(request, 'quiz/quiz_result.html')


