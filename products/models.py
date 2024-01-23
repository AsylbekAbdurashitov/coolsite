from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to='images/')


# class Category(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.FloatField(default=1)
    bio = models.TextField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.firstname +" "+ self.lastname


class Site(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.FloatField(default=1)

    def __str__(self):
        return self.firstname +" "+ self.lastname


class Actress(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=1)
    intro = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT)
    info = models.TextField()

    def __str__(self):
        return self.name






