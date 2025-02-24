from django.db import models

'''This is the database table that stores the sql queries'''
class SqlInjection(models.Model):
    statement = models.CharField(max_length=255, blank=False)
    
    class Meta:
        db_table = 'sqlinjection'