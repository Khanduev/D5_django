from django.urls import path
from .views import Articles, Search, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('', Articles.as_view()),
    path('search/', Search.as_view()),

    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # Ссылка на детали товара
    path('add/', ArticleCreateView.as_view(), name='article_create'),  # Ссылка на создание товара
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
]