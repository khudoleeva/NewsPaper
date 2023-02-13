from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .filters import PostFilter
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver


class PostList(ListView):
	model = Post
	template_name = 'news.html'
	context_object_name = 'posts'
	ordering = ['-date_post']
	paginate_by = 5

	def post(self, request, *args, **kwargs):
		category_id = request.POST['cat']
		re = Post.objects.filter(category=category_id)
		ca = Category.objects.all()
		cat_name = request.POST['btn']

		return render(request, 'news.html', {'posts': re, 'categ':ca, 'cat_name':cat_name})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categ'] = Category.objects.all()
		return context

@login_required
def Subscribers(request):
	user = request.user
	if request.POST['sub']:
		subs = request.POST['sub']
		category_sub = Category.objects.get(name_category=subs)
		category_sub.subscribers.add(user.id)
		category_sub.save()
	return redirect('/news/user/')

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

