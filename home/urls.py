from django.urls import path
from home import views


urlpatterns = [
    path('',views.index,name="products"),
    path('cart1/',views.cart,name="cart"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Pass product_id as an integer
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Pass product_id for removing
]




