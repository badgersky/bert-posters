from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Poster(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/', height_field=height, width_field=width, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-date_add',)
        