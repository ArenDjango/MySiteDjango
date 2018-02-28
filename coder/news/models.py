from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)#Максимальная длина строки 120
    post = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(blank=True, upload_to='articles_images/', help_text='300x300px', verbose_name='Ссылка картинки')

    def __str__ (self):
        return self.title
