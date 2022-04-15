from django.urls import path

from .views import CreatePollsView, CreateQuestionsView, PollsDetailView, PollsView, QuestionView

urlpatterns = [
    path('polls/', PollsDetailView.as_view(), name='polls detail view'),
    path('polls/<int:pk>/', PollsView.as_view(), name='polls view'),
    path('polls/create/', CreatePollsView.as_view(), name='create poll'),
    path('questions/<int:pk>/', QuestionView.as_view(), name='question'),
    path('questions/create/', CreateQuestionsView.as_view(), name='create question'),
]