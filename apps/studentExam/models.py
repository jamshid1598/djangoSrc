from django.db import models

# Create your models here.

# Moliya va buxgalteriya hisobi fakulteti bo'yicha talabalar o'qishini ko'chirish (tiklash) jarayonida aniqlangan fanlar farqi bo'yicha ma'lumot
# Moliya va buxgalteriya hisobi fakulteti bo'yicha talabalar o'qishini ko'chirish (tiklash) jarayonida aniqlangan fanlar farq


class Student(models.Model):
    l_name = models.CharField(max_length=255, blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    m_name = models.CharField(max_length=255, blank=True, null=True)
    
    group = models.CharField(max_length=10, blank=True, null=True) 
    direction = models.CharField(max_length=255, blank=True, null=True)
    
    fan1 = models.CharField(max_length=255, blank=True, null=True)
    fan2 = models.CharField(max_length=255, blank=True, null=True)
    fan3 = models.CharField(max_length=255, blank=True, null=True)
    fan4 = models.CharField(max_length=255, blank=True, null=True)
    fan5 = models.CharField(max_length=255, blank=True, null=True)
    fan6 = models.CharField(max_length=255, blank=True, null=True)
    fan7 = models.CharField(max_length=255, blank=True, null=True)
    fan8 = models.CharField(max_length=255, blank=True, null=True)
    fan9 = models.CharField(max_length=255, blank=True, null=True)
    fan10 = models.CharField(max_length=255, blank=True, null=True)
    fan11 = models.CharField(max_length=255, blank=True, null=True)
    fan12 = models.CharField(max_length=255, blank=True, null=True)
    fan13 = models.CharField(max_length=255, blank=True, null=True)
    fan14 = models.CharField(max_length=255, blank=True, null=True)
    fan15 = models.CharField(max_length=255, blank=True, null=True)
    fan16 = models.CharField(max_length=255, blank=True, null=True)
    fan17 = models.CharField(max_length=255, blank=True, null=True)
    fan18 = models.CharField(max_length=255, blank=True, null=True)
    fan19 = models.CharField(max_length=255, blank=True, null=True)
    fan20 = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.l_name} {self.f_name} {self.m_name}"