from django.contrib import admin
from django.urls import path
from website.views import post_list, post_retrieve, post_create, post_update, post_delete, post_main, post_contact, post_we
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/contact/', post_contact),
    path('main/we/', post_we), 
    path('main/', post_main),  
    path('main/buy/', post_list),
    path('main/<int:pk>/', post_retrieve),
    path('main/sell/', post_create),
    path('main/<int:pk>/update/', post_update),
    path('main/<int:pk>/delete/', post_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)