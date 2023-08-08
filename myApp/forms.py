from django import forms

from myApp.models import Programmers


class programForm(forms.ModelForm):

    class Meta:
        model = Programmers
        fields = "__all__"
