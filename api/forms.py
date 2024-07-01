from django import forms
from .models import DeveloperResponse

class DeveloperResponseForm(forms.ModelForm):
    class Meta:
        model = DeveloperResponse
        fields = [
            'salary', 'experience', 'employment_type', 'team_status', 'team_size',
            'company_size', 'weekly_hours', 'industry', 'languages', 'dev_type',
            'development_type', 'project_tools', 'agile_methods', 'job_satisfaction',
            'job_stress', 'work_life_balance', 'job_motivation', 'professional_goal',
            'sport_activity', 'main_sport', 'favorite_sport'
        ]
