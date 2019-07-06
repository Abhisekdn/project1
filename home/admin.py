from django.contrib import admin

from home.models import Student
from home.models import Library
from home.models import Book
from home.models import Section
from home.models import Teacher


# Register your models here.
#admin.site.register(Student)
#admin.site.register(Book)
#admin.site.register(Section)
#admin.site.register(Teacher)
#admin.site.register(Library)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('book',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','timestamp','department')
    list_filter=('student_name','timestamp','department')
    fields=('student_name','department')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields=('teacher',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    search_fields=('section',)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    search_fields=('library_name','books')
    
