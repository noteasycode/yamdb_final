from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    fields = ('name', 'year', 'description', 'genre', 'category')
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'score')
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    fields = ('review', 'text')
    search_fields = ('review',)


admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
