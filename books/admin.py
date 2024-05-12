from django.contrib import admin
from .models import BookCategory,Book,BookSubCategory,Author,BookOption


admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BookSubCategory)
admin.site.register(Author)
admin.site.register(BookOption)
