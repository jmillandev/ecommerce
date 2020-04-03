from django.db import models

from users.models import User

class ShippingAddresses(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    reference = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zip_code

    @property
    def address(self):
        return f'{self.city} {self.state} {self.country}'

    def update_default(self, default=False):
        self.default = default
        self.save()