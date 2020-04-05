from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.common import OrderStatus

"""
A continuacion se lista los diferentes atributos que
podemos utilizar dependiendo de lca clase de la cual
heredemos.

AbstractUser
    - username
    - first_name
    - last_name
    - email
    - password
    - groups
    - user_permissions
    - is_staff
    - is_active
    - is_superuser
    - last_login
    - data_joined

AbstractBaseUser
    - id
    - password
    - last_login
"""
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    @property
    def shipping_address(self):
        return self.shippingaddresses_set.filter(default=True).first()

    @property
    def addresses(self):
        return self.shippingaddresses_set.all()

    def has_shipping_address(self):
        return self.shipping_address is not None

    def has_shipping_addresses(self):
        return self.shippingaddresses_set.exists()


class Customer(User):
    """
    Esta clase agrega funcionabilidad al Modelo User
    mas no genera una tabla adicional
    """
    class Meta:
        proxy = True
    
    def get_products(self):
        return list()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()