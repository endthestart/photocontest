import datetime

from django import forms
from .models import Profile, Event


class EventForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.filter(event_date__lte=datetime.datetime.today()))


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Profile