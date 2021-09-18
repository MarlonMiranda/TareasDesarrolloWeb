from django.contrib import admin
from django.urls import path, include
from estudiantes import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='index'),
    path('', include('estudiantes.urls')),

]
