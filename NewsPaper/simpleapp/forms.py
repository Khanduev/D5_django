from django.forms import ModelForm, BooleanField
from .models import Article


# Создаём модельную форму
class ArticleForm(ModelForm):
    check_box = BooleanField(label='Tuturu!')
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Article
        fields = ['name', 'description', 'category', 'creator', 'check_box']
