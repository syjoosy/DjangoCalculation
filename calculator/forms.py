from django import forms
from django.contrib.auth.forms import User
from .models import Expressions


class UserForm(forms.ModelForm):
    value = forms.CharField()
    expression = forms.CharField()
    # enterid = forms.IntegerField()
    # result = forms.IntegerField(null=True)
    # class Meta:
    #     model = User
    #     fields = ['value', 'expression']
    class Meta:
        model = Expressions
        fields = ['value', 'expression']

class RecieveResult(forms.ModelForm):
    enterid = forms.IntegerField()

    class Meta:
        model = Expressions
        fields = ['enterid']