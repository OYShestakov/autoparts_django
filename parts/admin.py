from django.contrib import admin
from .models import Subscriber, Part


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]

    class Meta:
        model = Subscriber


class PartAdmin(admin.ModelAdmin):
    list_display = ["artikul", "title", "mark", "model", "year", "price_incomplete", "price", "description"]
    # list_display = [field.name for field in Part._meta.fields] # вывод всех полей
    search_fields = ["artikul"]

    class Meta:
        model = Part


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Part, PartAdmin)

