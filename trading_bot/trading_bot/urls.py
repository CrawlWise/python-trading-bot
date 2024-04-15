from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('trade/', include('Trade.urls')),
    path('account/',include('Account.urls')),
    # path('', include('History.urls')),
    # path('', include('Portfolio.urls')),
]
