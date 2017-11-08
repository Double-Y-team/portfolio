from django.db import models


class News(models.Model):
    titel = models.CharField(max_length=256, help_text='max_length=256')
    text = models.CharField(max_length=1024, help_text='max_length=1024')
    img = models.ImageField(upload_to='news/')

    is_activ = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.titel

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
