from django.db import models


# Create your models here.
class DeveloperResponse(models.Model):
    salary = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=200, blank=True)
    employment_type = models.CharField(max_length=200, blank=True)
    team_status = models.CharField(max_length=200, blank=True)
    team_size = models.CharField(max_length=200, blank=True)
    company_size = models.CharField(max_length=200, blank=True)
    weekly_hours = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200, blank=True)
    languages = models.CharField(max_length=200, blank=True)
    dev_type = models.CharField(max_length=200, blank=True)
    development_type = models.CharField(max_length=200, blank=True)
    project_tools = models.CharField(max_length=200, blank=True)
    agile_methods = models.CharField(max_length=200, blank=True)
    job_satisfaction = models.CharField(max_length=200, blank=True)
    job_stress = models.CharField(max_length=200, blank=True)
    work_life_balance = models.CharField(max_length=200, blank=True)
    job_motivation = models.CharField(max_length=200, blank=True)
    professional_goal = models.CharField(max_length=200, blank=True)
    sport_activity = models.CharField(max_length=200, blank=True)
    main_sport = models.CharField(max_length=200, blank=True)
    favorite_sport = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Salaire: {self.salary}"
