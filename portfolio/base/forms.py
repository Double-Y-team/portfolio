from django.contrib.auth.models import User
from django import forms
from .models import *


class CommentForm(forms.Form):
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea,

    )


