from django.db import models


class Design(models.Model):
    titelbild = models.ImageField(upload_to='media/images/%Y/%m/%d', blank=True, null=True)
    icon = models.ImageField(upload_to='media/images/%Y/%m/%d', blank=True, null=True)
    titel = models.CharField(max_length=250)
    description = models.TextField()
    release_date = models.DateTimeField(auto_created=True)
    category = models.ForeignKey('Category')

    def __unicode__( self ):
        return self.titel + ', ' + str(self.release_date) + ', ' + self.description


class SampleImage(models.Model):
    design = models.ForeignKey(Design)
    image = models.ImageField(upload_to='media/images/%Y/%m/%d', blank=True, null=True)

    def __unicode__( self ):
        return self.design.titel + ', ' + self.image.name


class Category(models.Model):
    titel = models.CharField(max_length=250)

    def __unicode__( self ):
        return self.titel