from django.contrib import admin
from django.urls import path, include
from times import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('times/', include('times.urls')),
    path('', views.home, name='home'),
]
