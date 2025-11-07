from django.db import models

class Patient(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree = models.FloatField()
    age = models.IntegerField()
    result = models.CharField(max_length=50, blank=True)  # You can manually enter or leave blank

    def __str__(self):
        return f"{self.age} yrs | Glucose: {self.glucose}"
    