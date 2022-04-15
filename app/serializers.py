from rest_framework import serializers
from .models import Member, Poll, Question


class MemberSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Member
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
