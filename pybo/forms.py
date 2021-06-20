from django import forms
from .models import Question, Answer, Comment

class QuestionForm(forms.ModelForm): #폼
    class Meta:
        model = Question # 모델
        fields = ['subject','content']

        #
        # widgets = {
        #     'subject':forms.TextInput(attrs={'class':'form-control'}),
        #     'content':forms.TextInput(attrs={'class':'form-control', 'row':10}),
        # }


        labels = {
            'subject':'제목',
            'content':'내용'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

        labels = {
            'content':'답변'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글내용'
        }