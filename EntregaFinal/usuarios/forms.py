from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import PerfilUsuario


class EstiloBootstrapMixin:
    """Agrega la clase de Bootstrap a todos los campos del formulario."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            clase = "form-select" if isinstance(campo.widget, forms.Select) else "form-control"
            campo.widget.attrs.setdefault("class", clase)


class RegistroForm(EstiloBootstrapMixin, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Ya existe una cuenta registrada con ese email.")
        return email


class LoginForm(EstiloBootstrapMixin, AuthenticationForm):
    pass


class PerfilUsuarioForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ["bio", "avatar"]
        labels = {"bio": "Sobre mí", "avatar": "Imagen de perfil"}
        widgets = {"bio": forms.TextInput(attrs={"placeholder": "Contá algo sobre vos"})}
