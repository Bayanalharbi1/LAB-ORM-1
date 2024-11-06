from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),  
    path('base/', views.base, name='base'),  
    path('add/', views.add_post, name='add_post'),
    path('posts/', views.post_list, name='post_list'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),  # Fixed'detail.page'
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'), 
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
