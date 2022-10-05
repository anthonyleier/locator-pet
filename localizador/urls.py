from django.urls import path
from localizador import views

# localizador:post
app_name = 'localizador'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/search', views.search, name='search'),
    path('posts/<int:id>', views.post, name='post'),
]
