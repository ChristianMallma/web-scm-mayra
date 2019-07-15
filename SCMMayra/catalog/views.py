from django.shortcuts import render
from django.db.models import Q, Max, Min
from django.views.generic import ListView,DetailView,CreateView,DeleteView,TemplateView
from .models import Producto,Comentario,CarritoCompras
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Creando vistas del catálogo
class ListadoProducto(ListView):
    template_name = 'catalog/listado_productos.html'
    model = Producto
    paginate_by = 3

    def get_queryset(self):
        query = None

        if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
            query = Q(nombre=self.request.GET["nombre"])

        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(precio__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(precio__lte=int(float(self.request.GET['maximo'])))
            except:
                pass


        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(precio__gte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(precio__gte=int(float(self.request.GET['minimo'])))
            except:
                pass


        if query is not None:
            productos = Producto.objects.filter(query)
        else:
            productos = Producto.objects.all()
        return productos
    
    def get_context_data(self, **kwargs):
        context = super(ListadoProducto, self).get_context_data(**kwargs)
        context['maximo'] = Producto.objects.all().aggregate(Max('precio'))['precio__max']
        context['minimo'] = Producto.objects.all().aggregate(Min('precio'))['precio__min']
        return context

class DetalleProducto(DetailView):
    template_name = 'catalog/detalle.html'
    model = Producto

class ComentarioProducto(CreateView):
    model = Comentario
    fields = ('comentario','usuario','producto',)

    def get_success_url(self):
        return "/catalog/detalleProducto/{}/".format(self.object.producto.pk)

class Salir(LogoutView):
    next_page = reverse_lazy('homePage')

class Ingresar(LoginView):
	template_name = 'coreWebPage/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('homePage'))
		else:
			context = self.get_context_data(**kwargs)
			return self.render_to_response(context)

	def get_success_url(self):
		return reverse('homePage')

class AniadirCarrito(LoginRequiredMixin, CreateView):
    model = CarritoCompras
    fields = ("usuario","producto","precio")
    success_url = reverse_lazy("listadoProductos")
    login_url = 'ingresar'
    template_name="catalog/listado_productos.html"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print(form.errors)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class EliminarCarrito(LoginRequiredMixin,DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('listarCarrito')
    login_url = 'ingresar'

class ListarCarrito(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context

class ListarCarritoPendientes(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context

class ListarCarritoFinalizadas(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context

class DetallePago(TemplateView):
    template_name="catalog/detalle_pago.html"