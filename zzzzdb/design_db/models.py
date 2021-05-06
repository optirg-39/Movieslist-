from django.db import models
import uuid
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Collection'

class Movies(models.Model):
    collection = models.ManyToManyField(Collection)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # genres = ArrayField(models.CharField(max_length=200), blank=True, default='list')
    uuid = models.UUIDField(default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Films'

class Genres(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genre =models.CharField(max_length=100)

    class Meta:
        db_table = 'Genre'
