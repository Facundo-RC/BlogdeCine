from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Slugs que coinciden con otras rutas de la app y no pueden usarse para un post.
SLUGS_RESERVADOS = {"nuevo", "buscar"}

GENEROS = [
    ("accion", "Acción"),
    ("animacion", "Animación"),
    ("ciencia_ficcion", "Ciencia ficción"),
    ("comedia", "Comedia"),
    ("documental", "Documental"),
    ("drama", "Drama"),
    ("romance", "Romance"),
    ("suspenso", "Suspenso"),
    ("terror", "Terror"),
    ("otro", "Otro"),
]

PUNTUACIONES = [(numero, f"{numero} de 5") for numero in range(1, 6)]


class Post(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    pelicula = models.CharField(max_length=150, blank=True)
    genero = models.CharField(max_length=20, choices=GENEROS, blank=True)
    puntuacion = models.PositiveSmallIntegerField(choices=PUNTUACIONES, null=True, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generar_slug_unico()
        super().save(*args, **kwargs)

    def generar_slug_unico(self):
        base_slug = slugify(self.titulo)[:160] or "post"
        slug = base_slug
        contador = 1
        while slug in SLUGS_RESERVADOS or Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            contador += 1
            slug = f"{base_slug}-{contador}"
        return slug

    @property
    def estrellas(self):
        """Puntuación en estrellas, por ejemplo ★★★☆☆."""
        if not self.puntuacion:
            return ""
        return "★" * self.puntuacion + "☆" * (5 - self.puntuacion)

    def get_absolute_url(self):
        return reverse("detalle_post", kwargs={"slug": self.slug})
