from django import forms
from django.forms import ModelForm, TextInput
from .models import Task, Title


class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '68', 'placeholder': 'Type...' }))

    class Meta:
        model = Task
        exclude = ['user', ]


class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = '__all__'
