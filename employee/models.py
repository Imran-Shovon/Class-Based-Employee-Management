from django.db import models

# Create your models here.
GENDER = {
    ('M', 'M'),
    ('F', 'F')
}

JOBTYPE = {
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Fullstack', 'Fullstack'),
    ('Intern', 'Intern')
}


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    salary = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    jobtype = models.CharField(max_length=50, choices=JOBTYPE)

    def __str__(self):
        return self.name + self.email
