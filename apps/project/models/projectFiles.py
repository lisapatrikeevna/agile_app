from django.db import models


class ProjectFiles(models.Model):
    file_name = models.CharField(max_length=120)
    path_file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def count_of_files(self):
    #     return self.file.count()

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['-created_at']




