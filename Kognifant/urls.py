from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('KfV1/', include('KfV1.urls')),
    path('admin/', admin.site.urls),
]
