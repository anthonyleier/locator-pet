from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from locator.views import auth, main, posts
from locator.views.api import posts as postsAPI
from locator.views.api import users as usersAPI

urlpatterns = [
    path('', main.home, name='home'),
    path('dashboard/', main.dashboard, name="dashboard"),
    path('posts/search/', main.search, name='search'),

    path('posts/new/', posts.createPost, name="createPost"),
    path('posts/edit/<int:id>/', posts.updatePost, name="updatePost"),
    path('posts/delete/<int:id>/', posts.deletePost, name="deletePost"),
    path('posts/found/<int:id>/', posts.foundPost, name="foundPost"),
    path('posts/<slug:slug>/', posts.detailPost, name='detailPost'),

    path('register/', auth.registerForm, name="registerForm"),
    path('register/action/', auth.registerAction, name="registerAction"),
    path('login/', auth.loginForm, name="loginForm"),
    path('login/action/', auth.loginAction, name="loginAction"),
    path('logout/action/', auth.logoutAction, name="logoutAction"),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/posts/', postsAPI.PostList.as_view(), name='postList'),
    path('api/posts/<int:id>/', postsAPI.PostDetail.as_view(), name='postDetail'),

    path('api/users/', usersAPI.UserList.as_view(), name='userList'),
    path('api/users/<int:id>/', usersAPI.UserDetail.as_view(), name='userDetail'),
]
