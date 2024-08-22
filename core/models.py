from django.db import models

class field(models.Model):
    taskname=models.CharField(max_length=500,null='false',blank='false',verbose_name="Todo")
    def __str__ (self):
        return (f"Task:${self.taskname}")