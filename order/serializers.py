from rest_framework import serializers
from .models import Order,OrderItem,Buy,Rent
from user.serializers import UserListSerializer,AddressSerializer
from books.models import BookOption

class OrderSerializer(serializers.ModelSerializer):
    buyer=UserListSerializer()
    shipping_address=AddressSerializer()
    billing_address=AddressSerializer()
    class Meta:
        model=Order
        fields="__all__"

class OrderCreateSerializer(serializers.ModelSerializer):
    buyer=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Order
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    order= OrderSerializer()
    item= serializers.StringRelatedField()
    order_option= serializers.StringRelatedField()
    price= serializers.SerializerMethodField()
    cost= serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        # fields= ["id","order","item","quantity","price","cost","created_at","updated_at","order_option"]
        fields = "__all__"

    def get_price(self,obj):
        return obj.item.price
    
    def get_cost(self,obj):
        return obj.cost
    
class OrderItemCreateSerializer(serializers.ModelSerializer):
    # buyer=serializers.HiddenField(default=serializers.CurrentUserDefault())
    # order_items=OrderItemSerializer(many=True)
    order=serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    # order_option=serializers.PrimaryKeyRelatedField(queryset=BookOption.objects.all())

    class Meta:
        model= OrderItem
        fields= (
            "id",
            "item",
            "order",
            "quantity",
            "order_option",
        )
    
    def create(self,validated_data):
        # orders_data=validated_data.pop("order_items")
        # order=Order.objects.create(**validated_data)
        book = validated_data.get('item',None)
        order_item=OrderItem.objects.create(**validated_data)
        order_option_instance= validated_data.get("order_option")
        if order_option_instance == "Rent":
           rent_data = {
               "renter":self.context["request"].user,
               "book":book,
               "rent_date":validated_data["order"].created_at.date(),
               "return_date":None,
               "status":Rent.PENDING,
           }
           rent=Rent.objects.create(**rent_data)
        else:
            buy_data={"book": book}
            buy = Buy.objects.create(**buy_data)
            return order_item

        # for order_data in orders_data:
        #     OrderItem.objects.create(order=order, **order_data)
        #     return order
    
    def update(self , instance, validated_data):
        instance.item=validated_data.get("item",instance.item)
        instance.order_option=validated_data.get("order_option", instance.order_option)
        instance.quantity=validated_data.get("quantity",instance.quantity)
        instance.save()
        return instance