# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Article
from .filters import ArticleFilter
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class Articles(ListView):
    model = Article
    ordering = '-publication'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10


class Search(ListView):
    model = Article
    ordering = '-publication'
    template_name = 'search.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetailView(DetailView):
    template_name = 'sample_app/article_detail.html'
    queryset = Article.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_article',)
    template_name = 'sample_app/article_create.html'
    form_class = ArticleForm
    raise_exception = True


# дженерик для редактирования объекта
class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_article',)
    template_name = 'sample_app/article_create.html'
    form_class = ArticleForm
    raise_exception = True

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


# дженерик для удаления товара
class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_article',)
    template_name = 'sample_app/article_delete.html'
    queryset = Article.objects.all()
    success_url = '/news/'
    raise_exception = True

