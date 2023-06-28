from django.db import models
# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.Username