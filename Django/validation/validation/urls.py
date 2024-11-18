# validation/urls.py (your project URL config)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_validation.urls')),  # Include app's URLs
]
