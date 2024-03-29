from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='home-page'),
    path('history/', views.history, name='history'),
    path('detail/', views.detail, name='detail'),
    path('management/', views.component_list, name='management'),
    path('component/create/', views.component_create, name='component_create'),
]
