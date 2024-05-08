from django.urls import path
from .views import UserCreateView,SellerListView,BuyerListView,UserListView,UserRetrieveView,UserDeleteView,UserLogoutView,UserLoginView

urlpatterns=[
    path('create/',UserCreateView.as_view(),name='create-user'),
    path('',UserListView.as_view(),name='user-list'),
    path('buyer/',BuyerListView.as_view(),name='buyers-list'),
    path('seller/',SellerListView.as_view(),name='Seller-list'),
    path('<int:pk>/Retrieve/',UserRetrieveView.as_view(),name='Retrieve-list'),
    path('<int:pk>/Delete/',UserDeleteView.as_view(),name='Delete-list'),
    path('login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('logout/',UserLogoutView.as_view(),name='user-logout')
     
]