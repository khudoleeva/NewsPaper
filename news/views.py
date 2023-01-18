from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin

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

class PostCreate(PermissionRequiredMixin,CreateView):
	permission_required = ('news.add_post',)
	template_name = 'news_app/create.html'
	form_class = PostForm

class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = ('news.change_post',)
	template_name = 'news_app/create.html'
	form_class = PostForm
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Post.objects.get(pk=id)

class PostDelete(PermissionRequiredMixin,DeleteView):
	permission_required = ('news.delete_post',)
	template_name = 'news_app/post_delete.html'
	# queryset = Post.objects.all()
	success_url = '/news/'
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Post.objects.get(pk=id)

@login_required
def upgrade_me(request):
	user = request.user
	premium_group = Group.objects.get(name='authors')
	if not request.user.groups.filter(name='authors').exists():
		premium_group.user_set.add(user)
	return redirect('/news/user/')

class UserView(LoginRequiredMixin, TemplateView):
	template_name = 'user_info.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
		return context