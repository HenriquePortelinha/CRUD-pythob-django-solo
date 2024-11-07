from django.db import models

# Create your models here.

class User(models.Model):
    class Meta: 
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_password = models.CharField(max_length=100, default='')
    usar_name = models.CharField(max_length=100, default='')
    user_email = models.EmailField(max_length=100, unique=True, default='')
    user_age = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email} | Age: {self.user_age}'
    
class UserTasks(models.Model):
    class Meta:
        db_table = 'user_tasks'
        verbose_name = 'User Task'
        verbose_name_plural = 'User Tasks'
    user_nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100, default='')
    task_description = models.CharField(max_length=100, default='')
    task_status = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.task_name = self.task_name.capitalize()
        self.task_description = self.task_description.capitalize()
        super().save(*args, **kwargs)
    
