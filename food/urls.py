from . import views
from django.urls import path

app_name= 'food'
urlpatterns = [
    # food/
    path('', views.index, name='index'),

    # food/<int:location_id>/
    path('<int:location_id>/', views.detail, name="detail"),

    # food/add/
    path('add/', views.create_location, name='create_location'),

    # food/update/<int:id>/
    path('update/<int:id>/', views.update_location, name='update_location'),

    # food/delete/<int:id>/
    path('delete/<int:id>/', views.delete_location, name='delete_location'),

    path('kasten/<int:kasten_id>/', views.kasten_detail, name='kasten_detail'),

    path('update_all_quantities/<int:kasten_id>/', views.update_all_quantities, name='update_all_quantities'),

    path('kasten-product/edit/<int:pk>/', views.edit_kasten_product, name='edit_kasten_product'),

    path('product/create/', views.create_product, name='create_product')
]
