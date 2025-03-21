from django.shortcuts import render, redirect
from .models import Disciplina

def listar_disciplinas(request):
    if request.method == 'POST':
        nome_disciplina = request.POST.get('nome_disciplina')
        nome_professor = request.POST.get('nome_professor')
        
        # Criar uma nova disciplina e salvar no banco de dados
        nova_disciplina = Disciplina(nome_disciplina=nome_disciplina, nome_professor=nome_professor)
        nova_disciplina.save()
        
        # Redirecionar de volta para a página após salvar
        return redirect('listar_disciplinas')

    # Buscar todas as disciplinas para exibir na tabela
    disciplinas = Disciplina.objects.all()
    return render(request, 'escola/listar_disciplinas.html', {'disciplinas': disciplinas})

