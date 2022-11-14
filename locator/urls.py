from locator.views import mainPages, postSystem, loginSystem, profiles, api, apiUser
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/posts/', api.PostList.as_view(), name='postList'),
    path('api/posts/<int:id>/', api.PostDetail.as_view(), name='postDetail'),

    path('api/users/', apiUser.UserList.as_view(), name='userList'),
    path('api/users/<int:id>/', apiUser.UserDetail.as_view(), name='userDetail'),
]
