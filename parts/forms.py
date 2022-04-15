from django import forms
from .models import Subscriber, Part

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude =['']