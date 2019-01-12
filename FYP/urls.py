from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('index/', include('index.urls')),
    path('about/', include('about.urls')),
    path('events/', include('events.urls')),
    path('products/', include('products.urls')),
    path('services/', include('services.urls')),
    path('contactus/', include('contactus.urls')),
    path('login/', include('login.urls')),
]
