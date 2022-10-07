from django.urls import path
from locator import views

# locator:post
app_name = 'locator'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/search', views.search, name='search'),
    path('posts/<int:id>', views.post, name='post'),
]
