from django.forms import ModelForm, Select
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

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
class BasicSignupForm(SignupForm):

	def save(self, request):
		user = super(BasicSignupForm, self).save(request)
		basic_group = Group.objects.get(name='common')
		basic_group.user_set.add(user)
		return user