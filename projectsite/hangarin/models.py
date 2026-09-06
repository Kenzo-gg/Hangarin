from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Priority(BaseModel):
    priority_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority_name

class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    class Meta:
            verbose_name = "Category"
            verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Note(BaseModel):
    note_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()

    def __str__(self):
        return self.note_task.title

class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    sub_title = models.CharField(max_length=255)
    sub_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return self.sub_title