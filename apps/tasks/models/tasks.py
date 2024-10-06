# # папка tasks модель tasks
#
from django.contrib.auth.models import User
from django.db import models

# from apps.project.models import Project
from apps.project.models.project import Project
# from ..choises import Priority, Statuses
from apps.tasks.choises import Priority, Statuses
from apps.tasks.models.tag import Tag
from apps.tasks.utils.set_date_time import last_day_of_month


# from ..models import Tag
# from ..utils.set_date_time import last_day_of_month


class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=Statuses.choices, default=Statuses.NEW)
    priority = models.SmallIntegerField(choices=Priority.choices, default=Priority.MEDIUM[0])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(default=last_day_of_month)
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_tasks', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name, self.status

    class Meta:
        ordering = ['-deadline']
        unique_together = (('name', 'project'),)




















