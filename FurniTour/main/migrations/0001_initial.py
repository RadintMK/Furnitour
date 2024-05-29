# Generated by Django 5.0.6 on 2024-05-21 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название тура')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('price_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена от')),
                ('travel_time', models.DurationField(verbose_name='Время в пути')),
                ('excursion_time', models.DurationField(verbose_name='Время экскурсий')),
                ('stops_count', models.IntegerField(verbose_name='Количество остановок')),
                ('food_provided', models.CharField(max_length=255, verbose_name='Питание предоставляется')),
                ('transport_included', models.CharField(max_length=255, verbose_name='Транспорт включен')),
                ('image', models.ImageField(upload_to='tours/images/', verbose_name='Изображение тура')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(default='', max_length=255)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
            ],
        ),
    ]