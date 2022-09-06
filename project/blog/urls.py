from django.urls import path
from . import views

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('', views.post_list, name='post_list'),
]