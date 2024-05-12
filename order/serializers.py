from rest_framework import serializers
from .models import Order,OrderItem
from user.serializers import UserListSerializer,AddressSerializer

class OrderSerializer(serializers.ModelSerializer):
    buyer=UserListSerializer()
    shipping_address=AddressSerializer()
    billing_address=AddressSerializer()
    class Meta:
        model=Order
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    order=OrderSerializer()
    item=serializers.StringRelatedField()
    price=serializers.SerializerMethodField()
    cost=serializers.SerializerMethodField()

    class Meta:
        model=OrderItem
        fields=["id","order","item","quantity","price","cost","created_at","updated_at","order_option"]

    def get_price(self,obj):
        return obj.item.price
    
    def get_cost(self,obj):
        return obj.cost
    
class OrderCreateSerializer(serializers.ModelSerializer):
    buyer=serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=(
            "id",
            "buyer",
            "status",
            "order_items",
            "created_at",
            "updated_at",
        )
    
    def create(self,validated_data):
        orders_data=validated_data.pop("order_items")
        order=Order.objects.create(**validated_data)

        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)
            return order
    
    def update(self , instance, validated_data):
        orders_data=validated_data.pop("order_items",None)
        orders=list((instance.order_items).all())

        if orders_data:
            for order_data in orders_data:
                order=orders.pop(0)
                order.item=order_data.get("item",order.item)
                order.quantity= order_data.get("quantity",order.quantity)
                order.save()
            return instance