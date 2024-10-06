from django.db import models

from .projectFiles import ProjectFiles


# from apps.project.models.projectFiles import ProjectFiles


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ManyToManyField(ProjectFiles, related_name='project', blank=True, null=True)
    objects = models.Manager()

    @property
    def count_of_files(self):
        return self.file.count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
