from django.contrib import admin
from core.models import *


class DesignAdmin(admin.ModelAdmin):
    pass


class SampleImageAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Design, DesignAdmin)
admin.site.register(SampleImage, SampleImageAdmin)
admin.site.register(Category, CategoryAdmin)