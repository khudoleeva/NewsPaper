from django.urls import path
from .views import PostList, PostDetail,SearchPost,PostCreate,PostUpdate,PostDelete,UserView, Subscribers
from .views import upgrade_me

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view()),
    path('search', SearchPost.as_view()),
    path('add', PostCreate.as_view()),
    path('<int:pk>/edit', PostUpdate.as_view()),
    path('<int:pk>/delete', PostDelete.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('user/', UserView.as_view()),
    path('category/', Subscribers),
]
