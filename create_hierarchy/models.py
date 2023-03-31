from django.db import models


class Employee(models.Model):
    class PositionChoices(models.TextChoices):
        GOD = "god"
        SEO = "seo"
        LEAD = "lead"
        SENIOR = "senior"
        MIDDLE = "middle"
        JUNIOR = "junior"
        TRAINEE = "trainee"

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, choices=PositionChoices.choices)
    hire_date = models.DateField()
    email = models.EmailField()
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
