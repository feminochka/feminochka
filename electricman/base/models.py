from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField('О нас', max_length=20)
    image = models.ImageField('Картинка', upload_to='static/assets/images')
    separator = models.ImageField('Разделитель', upload_to='static/assets/images')
    subtitle1 = models.CharField('Заголовок', max_length=60)
    subtitle2 = models.CharField('Заголовок', max_length=60)
    subtitle3 = models.CharField('Заголовок', max_length=60)
    subtitle4 = models.CharField('Заголовок', max_length=60)
    text1 = models.TextField('Описание')
    text2 = models.TextField('Описание')
    text3 = models.TextField('Описание')
    text4 = models.TextField('Описание')
    icon1 = models.CharField('Иконка', max_length=30)
    icon2 = models.CharField('Иконка', max_length=30)
    icon3 = models.CharField('Иконка', max_length=30)
    icon4 = models.CharField('Иконка', max_length=30)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
