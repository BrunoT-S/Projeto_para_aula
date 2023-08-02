from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PessoasForm
from .models import Pessoas
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def main(request):
	variav = loader.get_template('index.html')
	return HttpResponse(variav.render())

def cadastro(request):
	form = PessoasForm()

	context = {"form":form}

	if request.method == "POST":
		form = PessoasForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Adicionado com sucesso!!!')
		else:
			print(form.errors)
		
	return render(request,"cadastro.html",context=context)

def visualizar(request):
	objetos = Pessoas.objects.all()
	context = {"obj":objetos}
	return render(request,'ver.html', context=context)

def Update(request, pk):

	dado = Pessoas.objects.get(id=pk)

	form = PessoasForm(instance=dado)


	if request.method == "POST":
		form = PessoasForm(request.POST, instance = dado)
		if form.is_valid():
			form.save()
			return redirect('ver')
		else:
			print(form.errors)
	
	context = {"form":form}

	return render(request,"Update.html",context=context)

def Delete(request, pk):

	obj = Pessoas.objects.get(id=pk)

	if request.method == "POST":
		obj.delete()
		return redirect('ver')
	
	context = {"obj":obj}

	return render(request,"Deletar.html",context=context)

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm (request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect("ver")
	else:
		form = UserCreationForm()
	return render(request, 'SignUp.html', { 'form': form })

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
		login(request, user)
		return redirect("ver")
	else:
		form = AuthenticationForm()
	return render(request, 'LogIn.html', { 'form': form })

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect("main")


@login_required(login_url="Login")
def painel_usuario(request):
	return render(request, "Pagina_usuario.html")
