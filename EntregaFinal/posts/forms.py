from django import forms

from usuarios.forms import EstiloBootstrapMixin

from .models import Post


class PostForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "pelicula", "genero", "puntuacion", "contenido", "imagen"]
        labels = {
            "titulo": "Título",
            "pelicula": "Película (opcional)",
            "genero": "Género (opcional)",
            "puntuacion": "Puntuación (opcional)",
            "contenido": "Contenido",
            "imagen": "Imagen (opcional)",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título del post"}),
            "pelicula": forms.TextInput(attrs={"placeholder": "Ej.: El secreto de sus ojos (2009)"}),
            "contenido": forms.Textarea(attrs={"rows": 10}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo
