from django.db import models

# Create your models here.
class AbstractbaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abtract = True

class contact(AbstractbaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name