# articles/views.py
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'  # Specify your template name here

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'  # Specify your template name here        

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body")  # Specify the fields you want to edit
    template_name = 'article_edit.html'  # Specify your template name here
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'  # Specify your template name here
    success_url = reverse_lazy('article_list')  # Redirect to the article list after deletion

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ("title", "body")  # Specify the fields you want to create
    template_name = 'article_new.html'  # Specify your template name here

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)