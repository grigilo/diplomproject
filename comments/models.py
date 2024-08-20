from django.db import models

from ad.models import Ad
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(User, verbose_name="Автор",
                               on_delete=models.CASCADE,)
    ad = models.ForeignKey(Ad, verbose_name="Обявление",
                           on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')

    def __str__(self):
        return f'Комментарий от {self.author} на объявление {self.ad}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
