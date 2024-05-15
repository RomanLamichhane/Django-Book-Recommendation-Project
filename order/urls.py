from .views import OrderCreateView,OrderRetrieveView,OrderUpdateView,OrderItemCreateView,OrderItemRetrieveView,OrderItemDeleteView,OrderItemUpdateView,OrderDeleteView,OrderView,OrderItemView
from django.urls import path

urlpatterns=[
    path("",OrderView.as_view(),name="order-item"),
    path("create/",OrderCreateView.as_view(),name="order-create"),
    path("<int:pk>/retrieve/",OrderRetrieveView.as_view(),name="order-retreive"),
    path("<int:pk>/update/",OrderUpdateView.as_view(),name="order-update"),
    path("<int:pk>/delete/",OrderDeleteView.as_view(),name="order-delete"),
    path("orderitem/",OrderItemView.as_view(),name="order-item"),
    path("orderitem/create/",OrderItemCreateView.as_view(),name="orderitem-create"),
    path("orderitem/<int:pk>/Retreive/",OrderItemRetrieveView.as_view(),name="orderitem-retreive"),
    path("orderitem/<int:pk>/update/",OrderItemUpdateView.as_view(),name="orderitem-update"),
    path("orderitem/<int:pk>/delete/",OrderItemDeleteView.as_view(),name="orderitem-delete"),
]