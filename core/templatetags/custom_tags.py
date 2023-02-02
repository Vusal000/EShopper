# from django.template import Library
# from core.models import advertisement, contact, product

# register = Library()

# @register.simple_tag
# def get_contact_all():
#     return contact.objects.all()

# @register.simple_tag
# def get_advertisement_all():
#     return advertisement.objects.all()

# @register.simple_tag
# def get_product_all(limit, offset):
#     return product.objects.all()[limit:offset]