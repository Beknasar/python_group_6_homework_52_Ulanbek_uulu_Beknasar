from django.core.validators import MinLengthValidator
from django.db import models



class Tasks(models.Model):
    summary = models.CharField(default='My title', max_length=200, null=False, blank=False, verbose_name='Название',
                               validators=[MinLengthValidator(10)])
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', blank=True, verbose_name='Тип')
    task_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    task_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class Status(models.Model):
    name = models.CharField(default='Task', max_length=20, null=False, blank=False, verbose_name='Название статуса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Статус'
        verbose_name_plural='Статусы'

class Type(models.Model):
    name = models.CharField(default='New', max_length=20, null=False, blank=False, verbose_name='Название типа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'