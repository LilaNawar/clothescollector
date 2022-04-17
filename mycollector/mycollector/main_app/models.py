from asyncio.windows_events import NULL
from secrets import choice
from django.db import models
from django.urls import reverse
# Create your models here.
OUTFIT = (
    ('W', 'Work'),
    ('C', 'Casual'),
    ('N', 'Night out')
)

class Pants(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pant_detail', kwargs={'pk': self.id})
        
    class Meta:
      ordering = [-1]


class Top(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    # pants = models.ManyToManyField(Pant)
    size = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'top_id': self.id})

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']



class Occasion(models.Model):
    top = models.ForeignKey(Top, on_delete=models.CASCADE)
    pant = models.ForeignKey(Pants, on_delete=models.CASCADE)



