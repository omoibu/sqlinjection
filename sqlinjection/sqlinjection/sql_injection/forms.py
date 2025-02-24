from django import forms

class InputForm(forms.Form):
    statement = forms.CharField(max_length=255)