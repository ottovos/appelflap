from django.db import models

class Customer(models.Model):
    sur_name=models.TextField(max_length=50)
    title=models.TextField(max_length=15)

    def __str__(self):
        return self.sur_name


class Project(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    project_name=models.TextField(max_length=15)
    project_location=models.TextField(max_length=50)

    def __str__(self):
        return self.customer