from django.urls import path
from locator import views

# locator:post
app_name = 'locator'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/search', views.search, name='search'),
    path('posts/<int:id>', views.post, name='post'),
]
