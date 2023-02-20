from datetime import date
from django.db import models
from django.urls import reverse

class Student(models.Model):
    document_id = models.CharField(primary_key=True, max_length=11, null=False, blank=False,)
    name = models.CharField(max_length=100, null=False, blank=False,)
    birth_date = models.DateField(null=False, blank=False, default=date(1990, 1, 1))
    
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})
    
class Course(models.Model):
    DIFFICULTY = (
        ("B", "Basic"),
        ("I", "Intermediate"),
        ("A", "Advanced"),
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=False)
    difficulty = models.CharField(max_length=1, default="B", choices=DIFFICULTY, null=False, blank=False)
    
    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

