from django.contrib import admin
from django.urls import path, include

from app.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),  # ← Это для API
]