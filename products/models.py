from django.db import models

# All Django models must inherit from models.Model
# everytime saving something in our models do,  [makemigrations and migrate]


class Product(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places= 2, max_digits= 10, default= 39.99)
    image = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title

    # on python2
    '''
    def __unicode__(self):
        return self.title
    '''