from django import forms
from . import Pomodoro

class PomodoroForm(forms.ModelForm):
    
    class Meta:
        model = Pomodoro
        fields = [
            "excercise",
            "rest",
            "sets"]