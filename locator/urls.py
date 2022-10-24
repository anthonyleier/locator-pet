from django.urls import path
from locator import views

# locator:post
app_name = 'locator'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/search', views.search, name='search'),
    path('posts/<int:id>', views.post, name='post'),
    path('register/form', views.registerForm, name="registerForm"),
    path('register/create', views.registerCreate, name="registerCreate"),
    path('login/form', views.loginForm, name="loginForm"),
    path('login/access', views.loginAccess, name="loginAccess"),
    path('logout/access', views.logoutAccess, name="logoutAccess"),
]
