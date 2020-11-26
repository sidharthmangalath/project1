from django.db import models
class customer(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.IntegerField()
    city=models.TextField()
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender=models.CharField(choices=GENDER_CHOICES,max_length=100)
    COUNTRY_CHOICES=(
        ('I','INDIA'),
        ('U','USA'),
        ('C','CANADA'),
        ('P','POLAND')
    )
    country=models.CharField(choices=COUNTRY_CHOICES,max_length=200)
    class Meta:
        verbose_name_plural="customer_details"
    def __str__(self):
        return self.Firstname
class StudentData(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    address=models.TextField()
    list1=[('Male','Male'),('Female','Female')]
    gender=models.CharField(max_length=23,choices=list1)
    favorite_fruit=models.TextField()


    class Meta:
        verbose_name_plural="student_details"


    def __str__(self):
        return self.name
# Create your models here.
class PlayerDetails(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    address=models.TextField(default='NA')
    list1 = [('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('Allrounder', 'Allrounder')]
    role=models.CharField(max_length=25,choices=list1)
    COUNTRY=models.TextField()
    password=models.CharField(max_length=25,default='NA')
    confirmpassword=models.CharField(max_length=25,default='NA')
    email=models.TextField(default='NA')
    fileupload=models.FileField(upload_to='documents',default='NA')
    class Meta:
        verbose_name_plural="player_details"

    def __str__(self):
        return self.name

class Student5(models.Model):
        name = models.CharField(max_length = 20)
        address = models.TextField()


