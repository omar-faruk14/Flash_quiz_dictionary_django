from django.contrib import admin
from django.urls import path, include
from Flash import views as Flash_View
from Quiz import views as Quiz_View
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Flash_View.home,name="Home"),
    path('flash-word/', Flash_View.flashcard_view, name='flash_word'),
    path('quiz/',Quiz_View.create_quiz,name='quiz'),
    path('create-quiz',Quiz_View.create_quiz_with_option,name='create-quiz'),
    path('quiz/start/', Quiz_View.start_quiz, name='start_quiz'),
    path('quiz/question/<int:question_id>/', Quiz_View.question_page, name='question_page'),
    path('quiz/result/', Quiz_View.quiz_result, name='quiz_result'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
