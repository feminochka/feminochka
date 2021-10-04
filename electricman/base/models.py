from django.db import models


# Create your models here.
class AboutCategory(models.Model):
    name = models.CharField('О нас', max_length=20)
    image = models.ImageField('Картинка', upload_to='static/assets/images')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.name


class Description(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    text = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=30)
    cat = models.ForeignKey('AboutCategory', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'

    def __str__(self):
        return self.title
