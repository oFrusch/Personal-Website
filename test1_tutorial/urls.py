from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('My_Songs/', include('My_Songs.urls')),
]
