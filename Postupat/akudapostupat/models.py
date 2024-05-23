from django.db import models

class EducationalInstitution(models.Model):
    full_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=10)
    type_educational = models.CharField(max_length=3)
    image = models.CharField(max_length=2083)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    main_advantages = models.TextField()
    budget_places = models.IntegerField()
    avg_certificate_score = models.FloatField()
    num_specialties = models.IntegerField()

class Specialty(models.Model):
    name = models.CharField(max_length=150)
    qualification = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    budget_places = models.IntegerField()
    duration = models.CharField(max_length=50)
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE)

class Contact(models.Model):
    website = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    working_hours = models.TextField()
    phone = models.CharField(max_length=20)
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE)
