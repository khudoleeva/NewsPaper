from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
	class Meta:
		model = Post
		fields = {
            'name_post': ['icontains'],
			'date_post':['lt'],
			'one_to_many_author__one_to_one_user':['exact'],
		}
# 'one_to_many_author':['icontains'],