from django.urls import path
from . import views

urlpatterns = [
    path('projects-list/', views.project_list),
    path('projects-detail/<int:pk>/', views.project_detail),
    path('project-image-list/', views.projectimage_list),
    path('project-image-detail/<int:pk>/', views.projectimage_detail),
    path('materials-list/', views.material_list),
    path('materials-detail/<int:pk>/', views.material_detail),
    path('doors-list/', views.door_list),
    path('doors-detail/<int:pk>/', views.door_detail),
    path('door-color-list/', views.doorcolor_list),
    path('door-color-detail/<int:pk>/', views.doorcolor_detail),
    path('locations-list/', views.location_list),
    path('locations-detail/<int:pk>/', views.location_detail),
]
