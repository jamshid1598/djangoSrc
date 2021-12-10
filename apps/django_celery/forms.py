from django import forms
from django.utils.translation import gettext_lazy as _
from .tasks import send_feedback_email_task


class EmailForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={"row":5}))
    honeypot = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def send_email(self):
        if self.cleaned_data['honeypot']:
            return False
        send_feedback_email_task.delay(self.cleaned_data['email'], self.cleaned_data['message'])