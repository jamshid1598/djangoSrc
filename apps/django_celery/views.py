from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import EmailForm
# Create your views here.


class SendFeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class    = EmailForm
    success_url = '/'
    
    def form_valid(self, form):
        form.send_email()
        return super(SendFeedbackView, self).form_valid(form)

