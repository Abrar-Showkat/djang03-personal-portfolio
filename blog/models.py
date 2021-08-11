from django.db import models

class Project_blog(models.Model):
    title=models.CharField(max_length=90)
    date=models.DateField()
    description=models.TextField(max_length=20000)

#This str function is used for admin page it now shows the title of blog in admin page instead of what it was showing before
    def __str__(self):
        return self.title

