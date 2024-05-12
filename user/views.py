from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from .serializers import UserCreateSerializer,UserListSerializer,UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }

class UserCreateView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token=get_tokens_for_user(user)
        return Response({'token':token,'msg':'SignUp Successful'}, status=status.HTTP_201_CREATED)
    
class SellerListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset= User.objects.all()

    def get_queryset(self):
        return User.objects.filter(seller=True)
    
class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer

class BuyerListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset=User.objects.all()

    def get_queryset(self):
        return User.objects.filter(seller=False)
    
class UserUpdateView(UpdateAPIView):
    serializer_class = UserListSerializer
    queryset=User

    
    
class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()
    
class UserDeleteView(DestroyAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()
    
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh":str(refresh),
            "access":str(refresh.access_token),
        } ,status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JWTAuthentication,)
    def post(self,request):
        refresh_token =  request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error':'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token=RefreshToken(refresh_token)
            token.blacklist()
        
        except Exception as e:
            return Response({'error':'Invalid refresh'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'success':'Successfully logged out'}, status=status.HTTP_200_OK)
            
    
    

    

            


    
# class BuyerUpdateView(UpdateAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(seller=True)

# class SellerUpdateView(UpdateAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(seller=True)
    
# class SellerRetrieveView(UpdateAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(seller=True)
    
# class BuyerRetrieveView(UpdateAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(seller=True)
    

    

    


    
