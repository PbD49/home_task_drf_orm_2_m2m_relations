from django.urls import path
from django.contrib import admin
from .views import articles_list


urlpatterns = [
    path('', articles_list, name='articles'),
    path('admin/', admin.site.urls),
]
