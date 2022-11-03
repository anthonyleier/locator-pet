from locator import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    path('posts/search', views.search, name='search'),
    path('posts/<int:id>', views.post, name='post'),

    path('register', views.registerForm, name="registerForm"),
    path('register/action', views.registerAction, name="registerAction"),

    path('login', views.loginForm, name="loginForm"),
    path('login/action', views.loginAction, name="loginAction"),

    path('logout/action', views.logoutAction, name="logoutAction"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('posts/new', views.createPost, name="createPost"),
    path('posts/edit/<int:id>', views.updatePost, name="updatePost"),
    path('posts/delete/<int:id>', views.deletePost, name="deletePost"),
]
