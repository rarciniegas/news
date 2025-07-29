# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"  # Specify the template to render for the home page 

# Create your views here.
