import random
from django.db import models 

import os

# All Django models must inherit from models.Model
# Everytime saving something in our models do,  [makemigrations and migrate]

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath) # returns basename of the file
    name, ext = os.path.splitext(base_name) # separates filename with its extension
    return name, ext

#for giving a new random pathname
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    # changing filename
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename= new_filename, ext= ext)
    return "products/{new_filename}/{final_filename}".format(new_filename= new_filename,final_filename= final_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places= 2, max_digits= 10, default= 39.99)
    image = models.ImageField(upload_to= upload_image_path , null= True, blank= True)
    featured = models.BooleanField(default= False)
    active = models.BooleanField(default= True)
    timestamp = models.DateTimeField(auto_now_add= True)
    is_digital = models.BooleanField(default= False)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title