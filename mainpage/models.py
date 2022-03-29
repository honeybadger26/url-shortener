from django.db import models
from django.urls import reverse
from uuid import uuid1

class URL(models.Model):
    short_url = models.CharField(max_length=500, unique=True)
    original_url = models.URLField(max_length=500, blank=False)
    times_used = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.short_url != '':
            super().save(*args, **kwargs)
            return

        # Keep trying until a unique id is found
        while True:
            new_url = str(uuid1())[:8]
            try:
                URL.objects.get(short_url=new_url)
            except URL.DoesNotExist:
                self.short_url = new_url
                super().save(*args, **kwargs)
                return

    def get_short_url(self):
        return reverse('mainpage:goto', kwargs={ 'short_url': str(self.short_url) })