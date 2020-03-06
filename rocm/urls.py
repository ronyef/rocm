from django.contrib import admin
from django.urls import path, include
from sensor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sensor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='user_profile'),
    path('logout/', views.logout_user, name='logout')
]
