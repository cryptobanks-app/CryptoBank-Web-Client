from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('auth/', include('usermgmt.urls')),
    path('transactions/', include('transactions.urls')),
    path('phoneservice/', include('phoneservice.urls')),
]
