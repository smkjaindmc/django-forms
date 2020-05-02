from django.db import models

# Create your models here.

class Data(models.Model):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    Choose = 'Choose'
    choose = [
        ('DAILY', DAILY),
        ('WEEKLY', WEEKLY),
        ('MONTHLY', MONTHLY)
    ]
    name = models.CharField(max_length=120)
    
    reports = models.CharField(
        max_length=8,
        choices=choose,
        default=Choose,
    )
    TEAM_CHOICES = (
   ('Raktima Mitra', 'Raktima Mitra'),
   ('Akansha', 'Akansha'),
   ('Amitesh Ranjan', 'Amitesh Ranjan'),
   ('Sheetal','Sheetal'),
   ('Kanika','Kanika'),
   ('Ajeet','Ajeet'),
   ('Shekar','Shekar')
)
    team_lead = models.CharField(max_length=25,choices=TEAM_CHOICES,blank=True)
    hours = models.DecimalField(decimal_places=1, max_digits=2, default = 2)
    today_progress = models.TextField(default = 'add')
    today_doc = models.FileField(upload_to = 'cv/images/', null = True)
    concern = models.TextField(default="your answer")
    next_plan = models.TextField(default="your answer")
    next_doc = models.FileField(upload_to = 'cv/images/', null = True)

