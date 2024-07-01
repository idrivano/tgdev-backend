import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DeveloperResponse


# Cette vue reçoit les données du quiz et les enregistre dans la base de données.
@csrf_exempt  # Décorateur pour désactiver la protection CSRF pour cette vue
def submit_quiz(request):
    if request.method == 'POST':  # Vérifie que la méthode de requête est POST
        try:
            # Charge les données JSON reçues dans la requête
            data = json.loads(request.body)
            
            # Liste des champs requis dans les données JSON
            required_fields = [
                'salary', 'experience', 'employment_type', 'team_status',
                'team_size', 'company_size', 'weekly_hours', 'industry',
                'languages', 'dev_type', 'development_type', 'project_tools',
                'agile_methods', 'job_satisfaction', 'job_stress',
                'work_life_balance', 'job_motivation', 'professional_goal',
                'sport_activity', 'main_sport', 'favorite_sport'
            ]
            
            # Vérifie que tous les champs requis sont présents dans les données
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Missing field: {field}'}, status=400)

            # Crée une nouvelle instance de DeveloperResponse avec les données reçues
            response = DeveloperResponse(
                salary=data['salary'],
                experience=data['experience'],
                employment_type=data['employment_type'],
                team_status=data['team_status'],
                team_size=data['team_size'],
                company_size=data['company_size'],
                weekly_hours=data['weekly_hours'],
                industry=data['industry'],
                languages=data['languages'],
                dev_type=data['dev_type'],
                development_type=data['development_type'],
                project_tools=data['project_tools'],
                agile_methods=data['agile_methods'],
                job_satisfaction=data['job_satisfaction'],
                job_stress=data['job_stress'],
                work_life_balance=data['work_life_balance'],
                job_motivation=data['job_motivation'],
                professional_goal=data['professional_goal'],
                sport_activity=data['sport_activity'],
                main_sport=data['main_sport'],
                favorite_sport=data['favorite_sport']
            )
            # Sauvegarde l'instance dans la base de données
            response.save()
            
            # Retourne une réponse JSON indiquant le succès
            return JsonResponse({'message': 'Quiz submitted successfully!'})
        except json.JSONDecodeError:
            # Gère l'erreur si les données reçues ne sont pas un JSON valide
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            # Gère l'erreur si un champ requis est manquant dans les données
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
    
    # Retourne une réponse d'erreur si la méthode de requête n'est pas POST
    return JsonResponse({'error': 'Invalid request method'}, status=405)
