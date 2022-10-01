from django.db import models
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=40)
    eage=models.IntegerField()
    eexp=models.IntegerField()
    esal=models.IntegerField()
    def __str__(self):
        return self.ename
