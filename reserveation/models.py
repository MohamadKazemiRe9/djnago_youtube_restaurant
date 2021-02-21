from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Reseravtion(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    phone = models.CharField(_("تلفن"), max_length=20)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email
    