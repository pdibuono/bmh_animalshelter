from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user/user_detail.html'
    context_object_name = 'user_in_view'
