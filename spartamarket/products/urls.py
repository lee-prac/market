from django.urls import path
from . import views

app_name="products"


urlpatterns = [
    path("",views.ProductListAPIView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductRUDAPIView.as_view(), name="product_detail"),
    path("<int:pk>/comments/", views.CommentListAPIView.as_view() , name="comment_list"),
    path("comments/<int:pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail"),
]