from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название тура")
    rating = models.FloatField(verbose_name="Рейтинг")
    price_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена от")
    travel_time = models.IntegerField(verbose_name="Время в пути")
    excursion_time = models.IntegerField(verbose_name="Время экскурсий")
    stops_count = models.IntegerField(verbose_name="Количество остановок")
    food_provided = models.CharField(max_length=255, verbose_name="Питание предоставляется")
    transport_included = models.CharField(max_length=255, verbose_name="Транспорт включен")
    image = models.ImageField(upload_to='tours/images/', verbose_name="Изображение тура")
    
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    session_id = models.CharField(max_length=255, default='')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)