from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('history/',views.history, name='history'),
    path('portfolio/',views.portfolio, name='portfolio')

]
