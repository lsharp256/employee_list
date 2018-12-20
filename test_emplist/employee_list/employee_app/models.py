from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.TextField(max_length=100)
    date_started = models.DateTimeField(auto_now=False)
    description = models.TextField(max_length=300, default='enter description here')
    photo = models.ImageField(upload_to='media',
                              default='default.jpg')

    def __str__(self):
        return "Employee: {} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()
