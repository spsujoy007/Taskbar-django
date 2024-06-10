from django.contrib import admin
from django.urls import path, include
from .views import home, tasks
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('showtasks/', tasks, name='showtasks'),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
