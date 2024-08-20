from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название товара")
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to="ad/", verbose_name="Изображение",
                              **NULLABLE)
    create_at = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Дата создания")
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    author = models.ForeignKey(User, verbose_name="автор", **NULLABLE,
                               on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
