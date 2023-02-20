from django.contrib import admin

from alunos.models import Course, Student

# Register your models here.
class Students(admin.ModelAdmin):
    list_display = ("document_id", "name", "birth_date")
    list_display_links = ("document_id", "name")
    list_per_page = 20
    search_fields = ("document_id", "name")

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ("id", "title", "description", "difficulty")
    list_display_links = ("id", "title",)
    list_per_page = 20
    search_fields = ("id", "title",)

admin.site.register(Course, Courses)