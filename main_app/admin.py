from django.contrib import admin
from .models import Guns, Category
# Register your models here.


class GunsAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'time_create', 'photo', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('photo', 'is_published')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Guns, GunsAdmin)
admin.site.register(Category)
