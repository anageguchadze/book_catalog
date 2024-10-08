from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_year', 'genre', 'brief_info')
    # list_per_page = 2
    actions = []

    @admin.display(description='description: ')
    def brief_info(self, catalog: Book):
        return f'Desctription: {len(catalog.genre)}'

    # @admin.action(description='mark by published_year')
    # def select_years(self, request, queryset):
    #     queryset.update(published_year=Book.Status)



# Register your models here.
# admin.site.register(Book, BookAdmin)