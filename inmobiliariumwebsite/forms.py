from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.Form):
    correo = forms.EmailField(required=True, help_text='Required.', label='Correo', widget=forms.EmailInput(attrs={'placeholder': 'Correo'}))
    telefono = forms.CharField(max_length=15, required=False, label='Teléfono', widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    nombre = forms.CharField(max_length=50, required=True, help_text='Required.', label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    mensaje = forms.CharField(max_length=500, required=True, help_text='Required.', label='Mensaje', widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'rows': 5}))

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if field_name == 'mensaje':
                field.widget.attrs.update({'class': 'textarea'})


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, required=False, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))

    username = forms.CharField(max_length=30, required=True, help_text='Required.', label='Usuario', widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))

    password1 = forms.CharField(max_length=30, required=True, help_text='Required.', label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    password2 = forms.CharField(max_length=30, required=True, help_text='Required.', label='Repetir contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})