from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.cache import cache

class Author(models.Model):
	rating_author = models.IntegerField(default=0)
	one_to_one_user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.one_to_one_user.username}'
	def update_rating(self):
		postRating = self.post_set.all().aggregate(sumR = Sum('rating_post'))
		postR=0
		postR += postRating.get('sumR')
		commentRating = self.one_to_one_user.comment_set.all().aggregate(sumC = Sum('rating_comment'))
		comR= 0
		comR += commentRating.get('sumC')
		self.rating_author = postR*3 + comR
		self.save()

class Category(models.Model):
	name_category = models.CharField(max_length=255, unique=True)
	subscribers = models.ManyToManyField(User, through="AuthorCategory")
	def __str__(self):
		return f'{self.name_category}'

class AuthorCategory(models.Model):
	in_user = models.ForeignKey(User, on_delete=models.CASCADE)
	in_category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Post(models.Model):
	article = 'a'
	news = 'n'
	list_type = [(article, "статья"), (news, "новость")]
	type_post = models.CharField(max_length=1, choices=list_type, default=news)
	date_post = models.DateTimeField(auto_now_add=True)
	rating_post = models.IntegerField(default=0)
	name_post = models.CharField(max_length=255)
	text_post = models.TextField()
	one_to_many_author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category, through="PostCategory")

	def like(self):
		self.rating_post += 1
		self.save()

	def dislike(self):
		self.rating_post -= 1
		self.save()

	def preview(self):
		return self.text_post[:124] + "..."
	def __str__(self):
		return f'{self.name_post.title()}: {self.text_post[:20]}'
	def get_absolute_url(self):
		return f'/news/{self.id}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		cache.delete(f'new-{self.pk}')

class PostCategory(models.Model):
	in_category = models.ForeignKey(Category, on_delete=models.CASCADE)
	in_post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
	rating_comment = models.IntegerField(default=0)
	text_comment = models.TextField()
	date_comment = models.DateTimeField(auto_now_add=True)
	one_to_many_post = models.ForeignKey(Post, on_delete=models.CASCADE)
	one_to_many_user = models.ForeignKey(User, on_delete=models.CASCADE)

	def like(self):
		self.rating_comment += 1
		self.save()

	def dislike(self):
		self.rating_comment -= 1
		self.save()





# Create your models here.
