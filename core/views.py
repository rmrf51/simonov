from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from .models import Book





@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Book
    template_name = 'home.html'

    def get_queryset(self):
        return
