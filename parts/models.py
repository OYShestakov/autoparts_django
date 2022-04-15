from django.db import models
import datetime

from django.utils import timezone


class Subscriber(models.Model):
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    email = models.EmailField(verbose_name='Почта')
    name = models.CharField(max_length=128, verbose_name='Имя')

    def __str__(self):
        return 'Пользователь: %s | Email: %s' % (self.name, self.email)

class Part(models.Model):
    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    artikul = models.CharField(max_length=50, verbose_name='Артикул поставщика', blank=True, null=True)
    konstruct_number = models.CharField(max_length=50, verbose_name='Номер производителя', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название детали', blank=True, null=True)
    mark = models.CharField(max_length=100, verbose_name='Марка автомобиля', blank=True, null=True)
    model = models.CharField(max_length=100, verbose_name='Модель автомобиля', blank=True, null=True)
    kuzov = models.CharField(max_length=100, verbose_name='Кузов автомобиля', null=True, blank=True)
    korobka = models.CharField(max_length=100, verbose_name='Коробка передач', null=True, blank=True)
    engine_mark = models.CharField(max_length=100, verbose_name='Маркировка двигателя', null=True, blank=True)
    engine_type = models.CharField(max_length=100, verbose_name='Тип двигателя', null=True, blank=True)
    engine_tints = models.CharField(max_length=100, verbose_name='Объем двигателя', null=True, blank=True)
    peculiarities_engine = models.CharField(max_length=100, verbose_name='Особенности двигателя', null=True, blank=True)
    napravlenie = models.CharField(max_length=100, verbose_name='Направление', null=True, blank=True)
    storona = models.CharField(max_length=100, verbose_name='Сторона', null=True, blank=True)
    cvet_kuzova = models.CharField(max_length=100, verbose_name='Цвет автомобиля', null=True, blank=True)
    year = models.IntegerField(verbose_name='Год выпуска', null=True, blank=True)
    price_incomplete_usd = models.DecimalField(verbose_name='Цена комплекта в $', max_digits=9, decimal_places=2, null=True, blank=True)
    price_usd = models.DecimalField(verbose_name='Цена в $', max_digits=9, decimal_places=2, null=True, blank=True)
    price_incomplete = models.DecimalField(verbose_name='Цена комплекта RUB', max_digits=9, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена RUB', max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    sostoyanie = models.CharField(max_length=250, verbose_name='Состояние', null=True, blank=True)
    part_url = models.CharField(max_length=100, verbose_name='URL запчасти', null=True, blank=True)
    part_photo = models.CharField(max_length=400, verbose_name='Фото запчасти', null=True, blank=True)
    auto_photo = models.CharField(max_length=400, verbose_name='Фото автомобиля', null=True, blank=True)
    vin = models.CharField(max_length=200, verbose_name='Вин номер', null=True, blank=True)
    type_block = models.CharField(max_length=100, verbose_name='Тип блока', null=True, blank=True)
    date_buy_new = models.DateTimeField(verbose_name='Дата приобретения новой', null=True, blank=True)
    add_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __repr__(self):
        add_date = datetime.datetime.strftime(datetime.datetime.fromtimestamp(self.add_date), "%d.%m.%y %H:%M")
        return f'{self.id} || {self.artikul} || {self.konstruct_number} || {self.title} || {self.mark} || {self.model} ' \
               f'|| {self.kuzov} || {self.korobka} || {self.engine_mark} || {self.engine_type} || {self.engine_tints} ' \
               f'|| {self.napravlenie} || {self.storona} || {self.cvet_kuzova} || {self.year} || {self.price} ' \
               f'|| {self.discription} || {self.sostoyanie} || {self.vin} || {self.part_url} || {self.part_photo} ' \
               f'|| {self.auto_photo} || {add_date}'

    def __str__(self):
            return '%s %s %s' % (self.artikul, self.title, self.price)