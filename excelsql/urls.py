from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home_page_url'),
    path('import/', export_to_sqlite, name='export_to_sqlite_url')



]