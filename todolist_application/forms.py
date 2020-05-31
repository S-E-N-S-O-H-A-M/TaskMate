from django import forms
from todolist_application.models import Tasklist

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasklist
        fields=['task','done']