from django.db import models

class DishListModel(models.Model):
    CATEGORY = (
        ('Пицца', 'Пицца'),
        ('Напитки', 'Напитки'),
        ('Другая еда', 'Другая еда')
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название блюда')
    image = models.ImageField(upload_to='dishes/', verbose_name='Добавьте фото')
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.TextField(blank=True, verbose_name='Описание блюда')
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Orders(models.Model):
    dish = models.CharField(max_length=100, verbose_name='Название блюда')
    time = models.TimeField(verbose_name='Время заказа')
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.dish


class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide