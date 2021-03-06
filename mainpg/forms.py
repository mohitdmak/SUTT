from django import forms

from .models import Question, Answers, Profile

from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

class answerForm(forms.ModelForm):
    ans = forms.Textarea
    class Meta:
        model=Answers
        
        fields=['ans']

class UserUpdateForm(forms.ModelForm):
    Name = forms.CharField
    Contact_Email=forms.EmailField()
    Bio = forms.Textarea
    Twitter_Handle = forms.CharField(required=False)
    Instagram_Handle = forms.CharField(required=False)
    Github_Handle = forms.CharField(required=False)
    Linkedin_Handle = forms.CharField(required=False)
    class Meta:
        model=Profile
        fields=['Name','Contact_Email','Bio','Twitter_Handle','Instagram_Handle','Github_Handle','Linkedin_Handle']

class UserPicUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['dp']