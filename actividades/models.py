from django.db import models

class Actividades(models.Model):

    def __str__(self):
        return '%s %s' % (self.value, self.unit)