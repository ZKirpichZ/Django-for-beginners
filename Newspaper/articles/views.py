from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from . import models


# Create your views here.
class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'
    
    
class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body',]
    template_name = 'article_edit.html'
    
class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    
    success_url = reverse_lazy('article_list')
    
    
class ArticleCreateView(CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author',]