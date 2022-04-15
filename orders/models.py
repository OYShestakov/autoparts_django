from django.db import models
from django.db.models.signals import post_save

from parts.models import Part


class Status(models.Model):
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    name = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name='Имя статуса')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return "Статус %s" % self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    total_amount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа', default=0)
    customer_name = models.CharField(max_length=64, verbose_name='Имя', blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None, verbose_name='Почта')
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None, verbose_name='Телефон')
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Адрес доставки')
    comments = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий к заказу')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статуc заказа')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, blank=True, null=True, default=None, on_delete=models.CASCADE)
    count_part = models.IntegerField(default=1, verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    total_amount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма', default=0)
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return '%s' % self.part.title

    def save(self, *args, **kwargs):
        price_per_item = self.part.price
        self.price_per_item = price_per_item
        self.total_amount_price = self.count_part * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_parts_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_parts_in_order:
        order_total_price += item.total_amount_price

    instance.order.total_amount_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)