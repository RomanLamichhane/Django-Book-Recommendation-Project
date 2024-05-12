from .models import Book,BookCategory,BookSubCategory,Author,BookOption
from rest_framework import serializers
from user.models import User

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCategory
        fields="__all__"

class BookSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= BookSubCategory
        fields="__all__"

class BookOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookOption
        fields="__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    category= serializers.StringRelatedField()
    sub_category=serializers.PrimaryKeyRelatedField(queryset=BookSubCategory.objects.all())
    author=serializers.StringRelatedField(many=True)
    available_to=serializers.SlugRelatedField(slug_field='slug',queryset=BookOption.objects.all())
    seller=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all)

    class Meta:
        model=Book
        fields="__all__"

    def get_seller():
        return User.objects.filter(seller=True)
    
class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"