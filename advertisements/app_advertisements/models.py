from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()


# Create your models here.
class Advertisements(models.Model):
    title = models.CharField("Заголовок",max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    negotiable = models.BooleanField("Торг",help_text="Отметьте если уместен торг")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    class Meta:
        db_table = 'advertisements'

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:green; font-weight: bold;"> Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:orange; font-weight: bold;"> Сегодня в {}</span>', updated_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='изображение')
    def image_display(self):
        if self.image:
            return format_html(
                '<img scr="{}" style="width: 55px;">', self.image.url
            )
        else:
            return 'No Image'
        



