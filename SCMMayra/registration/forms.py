from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creando clase para el formulario de creación
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    first_name = forms.CharField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    last_name = forms.CharField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    #Redefinimos la clase Meta, para extender el email
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    #Necesitamos validar que el usuario sea único para cada usuario (no se repita)
    def clean_email(self):  
        email = self.cleaned_data.get('email') #recuperando el email
        if User.objects.filter(email=email).exists(): #si email ya existe
            raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email
    
    #Validamos que el nombre de usuario sea único
    def clean_username(self):
        username=self.cleaned_data.get('username')#recuperamos los usernames registrados
        if User.objects.filter(username=username).exists():#si existe
            raise forms.ValidationError("El nombre de usuario ya existe, pruebe con otro")
        return username