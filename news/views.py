from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
	model = Post  # указываем модель, объекты которой мы будем выводить
	template_name = 'news.html'
	context_object_name = 'posts'
	queryset = Post.objects.order_by("-id")

class PostDetail(DetailView):
	model = Post
	template_name = 'new.html'
	context_object_name = 'new'