from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)