from django.urls import path, include
from blog.views import CategoryListView, PostByCategoryView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]