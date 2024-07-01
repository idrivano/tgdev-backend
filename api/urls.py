from django.urls import path
from .views import submit_quiz

urlpatterns = [
    path('submit-quiz/', submit_quiz, name='submit_quiz'),
]
