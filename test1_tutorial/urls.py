from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('My_Songs/', include('My_Songs.urls')),
    path('BlogApp/', include('BlogApp.urls')),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/', views.UserPageView.as_view(), name='user'),
    # path('update/', views.UpdateProfileView.as_view(), name='update')
]
