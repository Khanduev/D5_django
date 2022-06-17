from django import template


register = template.Library()


STRONG_WORDS = ["дизайн", "лесной"]


@register.filter()
def censor(text):
   if not isinstance(text, str):
       raise ValueError('Нельзя цензурировать не строку')

   for word in STRONG_WORDS:
       text = text.replace(word[1::], '*' * (len(word)-1))

   return text