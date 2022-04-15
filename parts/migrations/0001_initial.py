# Generated by Django 3.2.13 on 2022-04-15 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikul', models.CharField(blank=True, max_length=50, null=True, verbose_name='Артикул поставщика')),
                ('konstruct_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер производителя')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название детали')),
                ('mark', models.CharField(blank=True, max_length=100, null=True, verbose_name='Марка автомобиля')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель автомобиля')),
                ('kuzov', models.CharField(blank=True, max_length=100, null=True, verbose_name='Кузов автомобиля')),
                ('korobka', models.CharField(blank=True, max_length=100, null=True, verbose_name='Коробка передач')),
                ('engine_mark', models.CharField(blank=True, max_length=100, null=True, verbose_name='Маркировка двигателя')),
                ('engine_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип двигателя')),
                ('engine_tints', models.CharField(blank=True, max_length=100, null=True, verbose_name='Объем двигателя')),
                ('peculiarities_engine', models.CharField(blank=True, max_length=100, null=True, verbose_name='Особенности двигателя')),
                ('napravlenie', models.CharField(blank=True, max_length=100, null=True, verbose_name='Направление')),
                ('storona', models.CharField(blank=True, max_length=100, null=True, verbose_name='Сторона')),
                ('cvet_kuzova', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет автомобиля')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('price_incomplete_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена комплекта в $')),
                ('price_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена в $')),
                ('price_incomplete', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена комплекта RUB')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена RUB')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('sostoyanie', models.CharField(blank=True, max_length=250, null=True, verbose_name='Состояние')),
                ('part_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='URL запчасти')),
                ('part_photo', models.CharField(blank=True, max_length=400, null=True, verbose_name='Фото запчасти')),
                ('auto_photo', models.CharField(blank=True, max_length=400, null=True, verbose_name='Фото автомобиля')),
                ('vin', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вин номер')),
                ('type_block', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип блока')),
                ('date_buy_new', models.DateTimeField(blank=True, null=True, verbose_name='Дата приобретения новой')),
                ('add_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'Запчасть',
                'verbose_name_plural': 'Запчасти',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
    ]
