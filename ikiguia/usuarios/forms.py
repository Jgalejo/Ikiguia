from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


PREGUNTAS = [
    ("pregunta1", "Me gusta trabajar en equipo"),
    ("pregunta2", "Disfruto resolver problemas complejos"),
    ("pregunta3", "Prefiero tareas prácticas y manuales"),
    ("pregunta4", "Me interesan los temas científicos"),
    ("pregunta5", "Me gusta ayudar a otras personas"),
]

OPCIONES = [
    (1, "1 - Totalmente en desacuerdo"),
    (2, "2 - En desacuerdo"),
    (3, "3 - Neutral"),
    (4, "4 - De acuerdo"),
    (5, "5 - Totalmente de acuerdo")
]

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for clave, texto in PREGUNTAS:
            self.fields[clave] = forms.ChoiceField(
                label=texto,
                choices=OPCIONES,
                widget=forms.RadioSelect
            )

class IkigaiForm(forms.Form):
    ama_1 = forms.CharField(
        label="¿Qué actividad disfrutas tanto que perderías la noción del tiempo?",
        widget=forms.Textarea(attrs={'rows': 2})
    )
    ama_2 = forms.CharField(
        label="¿Qué harías gratis toda la vida si pudieras?",
        widget=forms.Textarea(attrs={'rows': 2})
    )

    bueno_1 = forms.CharField(
        label="¿En qué actividades te sientes competente o talentoso?",
        widget=forms.Textarea(attrs={'rows': 2})
    )
    bueno_2 = forms.CharField(
        label="¿Qué te dicen los demás que haces bien?",
        widget=forms.Textarea(attrs={'rows': 2})
    )

    pagado_1 = forms.CharField(
        label="¿Por qué habilidades o conocimientos te han pagado o podrían pagarte?",
        widget=forms.Textarea(attrs={'rows': 2})
    )
    pagado_2 = forms.CharField(
        label="¿Qué servicios podrías ofrecer profesionalmente?",
        widget=forms.Textarea(attrs={'rows': 2})
    )

    necesario_1 = forms.CharField(
        label="¿Qué problemas sociales o globales te gustaría resolver?",
        widget=forms.Textarea(attrs={'rows': 2})
    )
    necesario_2 = forms.CharField(
        label="¿Qué causa te motiva profundamente?",
        widget=forms.Textarea(attrs={'rows': 2})
    )


class CustomUserCreationForm(UserCreationForm):
    # Campos del modelo User que queremos usar y personalizar
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(required=True, label="Nombres")
    
    # Nuestro campo personalizado del modelo Profile
    fecha_de_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}) # Para un selector de fecha amigable
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'email', 'fecha_de_nacimiento')
    def save(self, commit=True):
        # Hacemos que el username sea el mismo que el email
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        
        if commit:
            user.save()
            # Guardamos los datos extra en el perfil del usuario
            profile = user.profile
            profile.fecha_de_nacimiento = self.cleaned_data["fecha_de_nacimiento"]
            profile.save()
            
        return user    

