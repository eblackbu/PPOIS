from django.db import models
import jsonfield


class Lab(models.Model):
    name = models.TextField(verbose_name='Название работы')

    def __str__(self):
        return f'Работа №{self.id} "{self.name}"'


class StudentsGroup(models.Model):
    name = models.TextField(verbose_name='Название группы')

    def __str__(self):
        return f'Группа {self.name}'


class LabResult(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='results', null=True)
    sgroup = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, related_name='results', null=True)
    data = jsonfield.JSONField()

    def __str__(self):
        return f'Работа №{self.lab_id} группы {self.sgroup_id}'
