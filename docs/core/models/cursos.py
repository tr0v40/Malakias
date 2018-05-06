from django.db import models

class Curso(models.Model):
  ID_Curso = models.AutoField(db_column='ID_Curso', primary_key=True)
  Nome = models.CharField(unique=True, max_length=40)
  class Meta:
        managed = False
        db_table = 'Curso'