from django.contrib import admin
from teensite.myapp.models import Blog, Category, Image
# from teensite.myapp.forms import ArticleModelAdminForm


class BlogAdmin(admin.ModelAdmin):
    excluded = ['posted']
    prepopulated_fields = {'slug': ('title',)}
   # form = ArticleModelAdminForm
    search_fields = ["title"]
    list_display = ["title"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title",]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Image, ImageAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)