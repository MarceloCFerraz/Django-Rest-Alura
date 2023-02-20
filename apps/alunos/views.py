from django.http import JsonResponse

# Create your views here.
def alunos(request):
    if request.method == "GET":
        alunos = {"id":1, "name": "Marcelo"}
        return JsonResponse(alunos)