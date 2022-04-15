from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member")

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.member.username


class Poll(models.Model):
    member = models.ForeignKey(Member, verbose_name='Member', on_delete=models.CASCADE, related_name='user')
    title = models.TextField(verbose_name='Title')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='Poll', on_delete=models.CASCADE, related_name='Poll')
    TYPE_CHOICES = (
        ("answer_with_text", "Answer with text"),
        ("answer_with_choice", "Answer with choice"),
        ("answer_with_some_choices", "Answer with some choices")
    )
    text = models.TextField(verbose_name='Text of question')
    type = models.CharField(verbose_name='Type of question', max_length=25, choices=TYPE_CHOICES)
    text_answer = models.TextField(verbose_name='Answer with text')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.text


