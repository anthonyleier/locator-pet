from locator.views import mainPages, postSystem, loginSystem, profiles, api
from django.urls import path

urlpatterns = [
    path('', mainPages.home, name='home'),
    path('dashboard/', mainPages.dashboard, name="dashboard"),

    path('posts/search/', postSystem.search, name='search'),
    path('posts/<int:id>/', postSystem.post, name='post'),

    path('posts/new/', postSystem.createPost, name="createPost"),
    path('posts/edit/<int:id>/', postSystem.updatePost, name="updatePost"),
    path('posts/delete/<int:id>/', postSystem.deletePost, name="deletePost"),

    path('register/', loginSystem.registerForm, name="registerForm"),
    path('register/action/', loginSystem.registerAction, name="registerAction"),

    path('login/', loginSystem.loginForm, name="loginForm"),
    path('login/action/', loginSystem.loginAction, name="loginAction"),

    path('logout/action/', loginSystem.logoutAction, name="logoutAction"),


    path('profile/<int:id>/', profiles.details, name="profileDetails"),
]

urlpatterns += [
    path('api/posts/', api.PostList.as_view(), name='postsList'),
    path('api/posts/<int:pk>/', api.PostDetail.as_view(), name='postDetail'),
]
