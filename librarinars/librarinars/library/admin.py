from django.contrib import admin

from librarinars.library.models import BookCategory, Book


class BookCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    search_fields = ('title',)
    list_filter = ('categories',)


admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)
