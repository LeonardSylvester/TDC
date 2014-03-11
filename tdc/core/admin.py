from django.contrib import admin
from core.models import *


class SampleImageInline(admin.TabularInline):
    model = SampleImage

class DesignAdmin(admin.ModelAdmin):
    inlines = [
        SampleImageInline,
    ]


class SampleImageAdmin(admin.ModelAdmin):
    pass


class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Design, DesignAdmin)
admin.site.register(SampleImage, SampleImageAdmin)
admin.site.register(Gallery, GalleryAdmin)