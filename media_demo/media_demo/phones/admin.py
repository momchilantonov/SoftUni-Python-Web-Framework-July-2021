from media_demo.phones.models import Phone, PhoneImage
from django.contrib import admin


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    pass