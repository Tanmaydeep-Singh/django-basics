import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User




def hello(request):
    return HttpResponse("The server is up on port 8000", status=200)

def get_items(request):
    users = User.objects.all()
    user_data = [{'username': user.username } for user in users]
    return JsonResponse({'users': user_data})

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        print("called")
        data = json.loads(request.body)
        name = data.get('name')
        print(name)
        # Here you can perform any necessary operations, such as saving to the database
        return JsonResponse({'message': 'Item created successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
