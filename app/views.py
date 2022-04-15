from rest_framework import generics

from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class PollsDetailView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'pk'


class CreatePollsView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'pk'


class CreateQuestionsView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ListQuestionsView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
