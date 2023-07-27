
from django.contrib import admin

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',include('contact.urls')),
    # path('insat',include('contact.urls')),
   path('',include('blog.urls')),
   path('about_us/',include('about.urls')),
]
