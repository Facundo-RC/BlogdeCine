from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def listado_posts(request):
    posts = Post.objects.select_related("autor")
    return render(request, "posts/listado_posts.html", {"posts": posts})


def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/detalle_post.html", {"post": post})


def buscar_posts(request):
    busqueda = request.GET.get("q", "").strip()
    resultados = Post.objects.none()
    if busqueda:
        resultados = Post.objects.select_related("autor").filter(
            Q(titulo__icontains=busqueda)
            | Q(pelicula__icontains=busqueda)
            | Q(contenido__icontains=busqueda)
        )
    return render(
        request,
        "posts/buscar_posts.html",
        {"busqueda": busqueda, "resultados": resultados},
    )


def obtener_post_del_autor(request, slug):
    """Devuelve el post solo si el usuario logueado es su autor."""
    post = get_object_or_404(Post, slug=slug)
    if post.autor != request.user:
        raise PermissionDenied
    return post


@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, "Post publicado.")
            return redirect(post)
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form, "titulo_pagina": "Nuevo post"})


@login_required
def editar_post(request, slug):
    post = obtener_post_del_autor(request, slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado.")
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(
        request,
        "posts/post_form.html",
        {"form": form, "titulo_pagina": "Editar post", "post": post},
    )


@login_required
def eliminar_post(request, slug):
    post = obtener_post_del_autor(request, slug)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post eliminado.")
        return redirect("listado_posts")
    return render(request, "posts/post_confirmar_borrado.html", {"post": post})
