from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import ComprobanteEnc,ComprobanteDet
from .forms import ComprobanteEncForm,ComprobanteDetForm,DetalleComprobanteFormSet
from django.contrib.auth.models import User


#Creando vista para mostrar clientes registrados
def cliente(request):
    clientes=User.objects.all()
    return render(request,"salidas/user_list.html",{"clientes":clientes})

# Creando las vistas a usar en el comprobante
class ComprobanteList(LoginRequiredMixin,ListView):
    model=ComprobanteEnc
    template_name="salidas/comprobanteenc_list.html"
    context_object_name="comprobantes"

class ComprobanteNew(PermissionRequiredMixin,CreateView):
    permission_required="salidas.add_comprobante"
    model=ComprobanteEnc
    login_url="home"
    template_name="salidas/comprobante_form.html"
    form_class=ComprobanteEncForm
    success_url=reverse_lazy("comprobantes_list")

    #cargar formulario vacío cuando se genere la vista
    def get(self,request,*args,**kwargs):
        self.object=None
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_comprobante_formset=DetalleComprobanteFormSet()
        return self.render_to_response(
            self.get_context_data(#enviamos a la plantilla
                form=form,
                detalle_comprobante=detalle_comprobante_formset
            )
        )

    #cuando le de click
    def post(self,request,*args,**kwargs):
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_comprobante=DetalleComprobanteFormSet(request.POST)

        if form.is_valid() and detalle_comprobante.is_valid():
            return self.form_valid(form,detalle_comprobante)
        else:
            return self.form_invalid(form,detalle_comprobante)
    
    def form_valid(self,form,detalle_comprobante):
        self.object=form.save()
        detalle_comprobante.instance=self.object
        detalle_comprobante.save()
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self,form,detalle_comprobante):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_comprobante=detalle_comprobante
            )
        )

class ComprobanteEdit(UpdateView):
    permission_required="salidas.change_comprobante"
    model=ComprobanteEnc
    login_url="home"
    template_name="salidas/comprobante_form.html"
    form_class=ComprobanteEncForm
    success_url=reverse_lazy("comprobantes_list")

    #Para que levante la misma plantilla después de guardar
    def get_success_url(self):
        return reverse("comprobante_edit",kwargs={'pk':self.get_object().id})
    
    #redefinimos el método get, para que cargue datos almacenados
    def get(self,request,*args,**kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalles=ComprobanteDet.objects.filter(comprobante=self.object).order_by('pk')
        detalles_data=[]
        for detalle in detalles:
            d={
                "producto":detalle.producto,
                "cantidad":detalle.cantidad,
                "precio":detalle.precio,
                "total":detalle.total
            }
            detalles_data.append(d)
        
        detalle_comprobante=DetalleComprobanteFormSet(initial=detalles_data)#carga inicial
        detalle_comprobante.extra += len(detalles_data)#para que renderice más espacio del que hay
        
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_comprobante=detalle_comprobante
            )
        )
    
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_comprobante=DetalleComprobanteFormSet(request.POST)
        if form.is_valid() and detalle_comprobante.is_valid():
            return self.form_valid(form,detalle_comprobante)
        else:
            return self.form_invalid(form,detalle_comprobante)
        
    def form_valid(self,form,detalle_comprobante):
        self.object=form.save()
        detalle_comprobante.instance=self.object
        ComprobanteDet.objects.filter(comprobante=self.object).delete()
        detalle_comprobante.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self,form,detalle_comprobante):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_comprobante=detalle_comprobante
            )
        )   