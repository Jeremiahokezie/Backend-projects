from django.db import models

# My model
class Guest(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=10000)
    Occupation = models.CharField(max_length=10000)
    Room_Category = models.CharField(max_length=100)
    Room_Type = models.CharField(max_length=100)
    Room_Number = models.IntegerField()
    Amount_Paid = models.CharField(max_length=100)
    Number_of_Nights = models.IntegerField()
    Start_Date = models.DateField()
    End_Date = models.DateField()
    

    def __str__(self):
        return self.Name
