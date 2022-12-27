from django.db import models

class Computers(models.Model):
    title = models.CharField('Название', max_length=200)
    inf = models.TextField('Информация', max_length=200)
    price = models.FloatField('Цена$', default=1)
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-price',)