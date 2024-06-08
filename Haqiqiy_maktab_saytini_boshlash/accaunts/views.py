from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class SignUp(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
class Home(TemplateView):
    template_name='index.html'
class news(TemplateView):
    template_name='news.html'
class connect(TemplateView):
    template_name='connect.html'