from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True,null=True)
    due_date = models.DateField(null=True,blank=True)
    category = models.CharField(default='general',max_length=50)
    is_complete = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"] #ordering by the created field

    def __str__(self):
        return self.title
