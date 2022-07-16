from django_filters import FilterSet
from .models import Article


class ArticleFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Article
        fields = {
                'name': ['icontains'],
                'publication': ['icontains'],
                'description': ['icontains'],
                'category': ['exact'],
                'creator': ['exact'],
        }  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)