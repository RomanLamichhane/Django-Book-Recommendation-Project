from django.shortcuts import render
from .models import OrderItem,Order
from .serializers import OrderItemSerializer,OrderCreateSerializer,OrderItemCreateSerializer,OrderSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView

class OrderView(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderCreateView(CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderCreateSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderItemSerializer

class OrderUpdateView(RetrieveUpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderItemSerializer

class OrderItemView(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemCreateSerializer

class OrderItemRetrieveView(RetrieveAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class OrderItemDeleteView(DestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class OrderDeleteView(DestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer


