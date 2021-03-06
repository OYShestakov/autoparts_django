from django.contrib import admin
from orders.models import Status, Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields] # вывод всех полей

    class Meta:
        model = Status

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] # вывод всех полей
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)