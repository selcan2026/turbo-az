from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    istifadeci = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    il = models.IntegerField()
    qiymet = models.DecimalField(max_digits=12, decimal_places=2)
    muherrik = models.CharField(max_length=50)
    yurus = models.IntegerField()
    shekil = models.ImageField(upload_to='cars/', blank=True, null=True)
    tarix = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marka + " " + self.model
