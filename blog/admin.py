from django.contrib import admin

from blog.models import Post, Tag, Author

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    list_filter = ("first_name", "last_name", "email_address")
admin.site.register(Author, AuthorAdmin )


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    list_filter = ("caption",)
admin.site.register(Tag, TagAdmin )


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title",)
admin.site.register(Post, PostAdmin)
