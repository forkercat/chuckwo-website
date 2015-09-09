from django.db import models

# Pet
class Pet(models.Model):
    name = models.CharField('Name', max_length=200)
    pic = models.CharField('Picture', max_length=200)
    hot = models.IntegerField('Hot', default=0)
    def __unicode__(self):
        return self.name

# Statistics
class Statistics(models.Model):
    name = models.CharField(max_length=200,default='chuck')
    visits = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
