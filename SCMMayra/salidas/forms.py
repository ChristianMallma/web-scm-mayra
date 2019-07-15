from django import forms
from .models import ComprobanteDet,ComprobanteEnc
from produccion.models import Disenio
from django.forms.models import inlineformset_factory

class ComprobanteEncForm(forms.ModelForm):
    fecha_factura=forms.DateInput()

    class Meta:
        model=ComprobanteEnc
        fields=["fecha_factura","cliente"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class":"form-control"
            })

class ComprobanteDetForm(forms.ModelForm):
    producto=forms.ModelChoiceField(
        queryset=Disenio.objects.filter(activo=True).order_by("nombre"),
        empty_label="Seleccione Producto"
    )

    class Meta:
        model=ComprobanteDet
        fields=["producto","cantidad","precio","total"]
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class":"form-control"
            })
        self.fields["total"].widget.attrs["readonly"]=True
    
    def clean_cantidad(self):
        cantidad=self.cleaned_data["cantidad"]
        if not cantidad:
            raise forms.ValidationError("Cantidad requerida")
        elif cantidad<=0:
            raise forms.ValidationError("Cantidad incorrecta")
        return cantidad
    
    def clean_precio(self):
        price=self.cleaned_data["precio"]
        if not price:
            raise forms.ValidationError("Precio requerida")
        elif price<=0:
            raise forms.ValidationError("Precio incorrecto")
        return price

DetalleComprobanteFormSet=inlineformset_factory(ComprobanteEnc,ComprobanteDet,form=ComprobanteDetForm,extra=4)