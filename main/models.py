from django.db import models


class Menu(models.Model):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    menu = models.ForeignKey(Menu, related_name='menu_items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)  # Используется CharField, а не URLField чтобы не требовалось указывать полный путь
    named_url = models.BooleanField(default=False)  # Если используется именованная ссылка, а не путь
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
