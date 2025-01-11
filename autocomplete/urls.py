
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('search/',index),
    path('get-names/',get_names),
    path('admin/', admin.site.urls),
]
