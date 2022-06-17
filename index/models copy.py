from django.db import models

# Create your models here.
class People(models.Model):
    Fullname = models.CharField(max_length=10000)
    Age = models.CharField(max_length=10000)
    Gender = models.CharField(max_length=10000)

    def __str__(self):
        return self.Fullname

class Addres(models.Model):
    Name_of_Company = models.CharField(max_length=10000)
    Address = models.CharField(max_length=10000)
    Owner = models.OneToOneField(People, on_delete=models.CASCADE) #The address of a place can only belong to that place

    def __str__(self):
        return self.Name_of_Company

class Doctor(models.Model):
    Name_of_Doctor = models.CharField(max_length=10000)
    Hospital = models.CharField(max_length=10000)
    Patient = models.ManyToManyField(People) #A doctor can have many persons as his patients and also a person can have more than one doctors at the same time 
    
    def __str__(self):
        return self.Name_of_Doctor

class Product(models.Model):
    Product = models.CharField(max_length=10000)
    Price = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.Product

class Bio(models.Model):
    Name_of_Family = models.CharField(max_length=10000)
    Biography = models.CharField(max_length=10000)
    Biographer = models.OneToOneField(People, on_delete=models.CASCADE) #The biography of a person only belongs to that person, it cannot be shared with another person

    def __str__(self):
        return self.Name_of_Family
        
    

