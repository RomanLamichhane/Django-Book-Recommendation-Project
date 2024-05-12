from django.urls import path
from .views import (
    BookCategoryListView,
    BookCategoryCreateView,
    BookCategoryRetrieveView,
    BookCategoryDeleteView,
    BookCategoryRetrieveView,
    BookCategoryUpdateView,

    BookSubCategoryRetrieveView,
    BookSubCategoryCreateView,
    BookSubCategoryDeleteView,
    BookSubCategoryListView,
    BookSubCategoryUpdateView,
   
   AuthorCreateView,
   AuthorDeleteView,
   AuthorListView,
   AuthorRetrieveView,
   AuthorUpdateView,

   BookOptionCreateView,
   BookOptionDeleteView,
   BookOptionListView,
   BookOptionRetrieveView,
   BookOptionUpdateView,

   BookCreateView,
   BookListView,
   BookRetrieveView,
   BookDeleteView,
   BookUpdateView,
   BookBuyRentView,
)

urlpatterns=[
    path("categories/",BookCategoryListView.as_view(),name="categories"),
    path("category/<int:pk>/",BookCategoryRetrieveView.as_view(),name="category-retrieve"),
    path("category/create/",BookCategoryCreateView.as_view(),name="category-create"),
    path("category/<int:pk>/update/",BookCategoryUpdateView.as_view(),name="category-update"),
    path("category/<int:pk>/delete/",BookCategoryDeleteView.as_view(),name="category-delete"),

    path("subcategories/",BookSubCategoryListView.as_view(),name="subcategories"),
    path("subcategory/<int:pk>/",BookSubCategoryRetrieveView.as_view(),name="subcategory-retrieve"),
    path("subcategory/create/",BookSubCategoryCreateView.as_view(),name="subcategory-create"),
    path("subcategory/<int:pk>/update/",BookSubCategoryUpdateView.as_view(),name="subcategory-update"),
    path("subcategory/<int:pk>/delete/",BookSubCategoryDeleteView.as_view(),name="subcategory-delete"),

    path("authors/",AuthorListView.as_view(),name="authors"),
    path("author/<int:pk>/",AuthorRetrieveView.as_view(),name="author-retrieve"),
    path("author/create/",AuthorCreateView.as_view(),name="author-create"),
    path("author/<int:pk>/update/",AuthorUpdateView.as_view(),name="author-update"),
    path("author/<int:pk>/delete/",AuthorDeleteView.as_view(),name="author-delete"),

    path("Bookoption/",BookOptionListView.as_view(),name="Book-option"),
    path("Bookoption/<int:pk>/",BookOptionRetrieveView.as_view(),name="Bookoption-retrieve"),
    path("Bookoption/create",BookOptionCreateView.as_view(),name="Bookoption-create"),
    path("Bookoption/<int:pk>/update/",BookOptionUpdateView.as_view(),name="Bookoption-update"),
    path("Bookoption/<int:pk>/delete/",BookOptionDeleteView.as_view(),name="Bookoption-delete"),

    

    path("books/",BookListView.as_view(),name="books"),
    path("book/<int:pk>/",BookRetrieveView.as_view(),name="book-retrieve"),
    path("book/create/",BookCreateView.as_view(),name="book-create"),
    path("book/<int:pk>/update/",BookUpdateView.as_view(),name="book-update"),
    path("book/<int:pk>/delete",BookDeleteView.as_view(),name="book-delete"),
    path("book-buy-rent/",BookBuyRentView.as_view(),name="book-buy-rent"),
]