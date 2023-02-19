from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.models import Products

@receiver(pre_save, sender=Products)
def product_pre_save(sender, instance, **kwargs):
    print('pre_save signals')
     