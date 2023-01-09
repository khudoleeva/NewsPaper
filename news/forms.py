from django.forms import ModelForm, Select
from .models import Post


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['type_post', 'name_post', 'text_post', 'one_to_many_author', 'category']
		labels = {
			'name_post': 'Заголовок',
			'type_post': 'Тип',
			'text_post': 'Текст',
			'one_to_many_author': 'Автор',
			'category': 'Категория'
		}
		# widgets = {
		# 	'category': Select(),
		# }