from django.shortcuts import render
from .forms import UserCreationFormWithEmail
from django.urls import reverse_lazy
from django import forms
from django.views.generic import CreateView
from django.shortcuts import redirect

#Creamos vista de registro
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail #formulario que mostrará en esta vista
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    #Método para recuperar el formulario
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificamos en tiempo real antes de recuperar el formulario
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repita la contraseña'})
        return form

def login_success(request):    
    if request.user.is_staff:
        # user is an admin
        return redirect("home")
    if request.user.get_username()=="provInsBas":
        return redirect("invInsumosB")
    if request.user.get_username()=="provInsExa":
        return redirect("invInsumosE")
    else:
        return redirect("homePage")

def logout_success(request):
    if request.user.is_staff:
        # user is an admin
        return redirect("home")
    else:
        return redirect("homePage")