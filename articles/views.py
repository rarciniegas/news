# articles/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'  # Specify your template name here

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'  # Specify your template name here        

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "body")  # Specify the fields you want to edit
    template_name = 'article_edit.html'  # Specify your template name here

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'  # Specify your template name here
    success_url = reverse_lazy('article_list')  # Redirect to the article list after deletion

class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "body", "author")  # Specify the fields you want to create
    template_name = 'article_new.html'  # Specify your template name here
    success_url = reverse_lazy('article_list')  # Redirect to the article list after creation
