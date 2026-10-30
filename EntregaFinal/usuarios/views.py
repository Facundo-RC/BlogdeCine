from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilUsuarioForm, RegistroForm
from .models import PerfilUsuario


def registro(request):
    if request.user.is_authenticated:
        return redirect("listado_posts")
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}! Tu cuenta fue creada.")
            return redirect("listado_posts")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})


@login_required
def perfil(request):
    perfil_usuario, _ = PerfilUsuario.objects.get_or_create(user=request.user)
    posts = request.user.posts.all()
    return render(request, "usuarios/perfil.html", {"perfil": perfil_usuario, "posts": posts})


@login_required
def editar_perfil(request):
    perfil_usuario, _ = PerfilUsuario.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("perfil")
    else:
        form = PerfilUsuarioForm(instance=perfil_usuario)
    return render(request, "usuarios/editar_perfil.html", {"form": form})
