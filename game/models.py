from django.db import models
# from django.conf import settings

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=20)
    power = models.IntegerField()

    def __str__(self):
        return self.name

# class Character(models.Model):
#     name = models.CharField(max_length=20)
#     weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='character_list')
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='character')

#     def __str__(self):
#         return f'{self.name} - {self.weapon.name}'
