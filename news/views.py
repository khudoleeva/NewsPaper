from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
	model = Post
	template_name = 'news.html'
	context_object_name = 'posts'
	ordering = ['-date_post']
	paginate_by = 5

class SearchPost(ListView):
	model = Post
	template_name = 'news_app/search.html'
	context_object_name = 'search'
	ordering = ['-date_post']
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
		return context


class PostDetail(DetailView):
	model = Post
	template_name = 'news_app/new.html'
	context_object_name = 'new'

class PostCreate(CreateView):
	template_name = 'news_app/create.html'
	form_class = PostForm
class PostUpdate(UpdateView):
	template_name = 'news_app/create.html'
	form_class = PostForm
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Post.objects.get(pk=id)

class PostDelete(DeleteView):
	template_name = 'news_app/post_delete.html'
	# queryset = Post.objects.all()
	success_url = '/news/'
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Post.objects.get(pk=id)
