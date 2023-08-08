from django.db import models

# Create your models here.


class Programmers(models.Model):
    Prog_Group_no = models.IntegerField()
    Prog_Roll_no = models.IntegerField(primary_key=True)
    Prog_Enroll_no = models.IntegerField()
    Prog_Name = models.CharField(max_length=100)
    Prog_Div = models.TextField()
    Prog_Details = models.TextField()

    class Meta:
        db_table = ("Programmers_Details")
