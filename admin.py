from django.contrib import admin
from django.forms import TextInput, Textarea

from .models import MenuItem, Category
from django.db import models


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    class Media:
        css = {
            'all': ('css/resize-widget.css',),
            # if you have saved this file in `static/css/` then the path must look like `('css/resize-widget.css',)`
        }


admin.site.register(Category)

