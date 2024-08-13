from django import forms

class ToDoForm(forms.Form):
    # Form fields
    detail= forms.CharField()
