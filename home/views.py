from django.views.generic import TemplateView
from django.shortcuts import render
from home import forms as Form
from django import forms
from home import calculations as calcu
from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse, HttpResponseRedirect
#from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.contrib.auth import get_user_model

#User = get_user_model()

class Calculadora1View(TemplateView):
    template_name = 'home/calculadora1.html'
    def get(self, request):
        return render(request, self.template_name, )

class Calculadora2View(TemplateView):
    template_name = 'home/calculadora2.html'
    def get(self, request):
        return render(request, self.template_name, )

class CharData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs_count = User.objects.all().count()
        labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [19, 23, 15, 32, 12, 2 ]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

class ContactoView(TemplateView):
    template_name = 'home/contacto.html'

    def get(self, request):
        form = Form.Contacto()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Contacto(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            #OPCION 1
            message = message + ". El correo es de: " + from_email
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['mich.montes@gmail.com'], fail_silently=False)
                except BadHeaderError:
                    text = 'Invalid header found.'
                text = 'Correo enviado con éxito'
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                text = 'Make sure all fields are entered and valid.'

            # subject, from_email, to = subject, from_email, 'lujosmich@gmail.com'
            # text_content = 'This is an important message.'
            # html_content = '<p>This is an <strong>important</strong> message.</p>' + from_email
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # try:
            #     msg.send()
            # except Exception as e:
            #     text = 'Ocurrió un error: '
            # else:
            #     text = 'Correo enviado con éxito'
            form = Form.Contacto()


        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class HomeView(TemplateView):
    template_name = 'home/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"customers":10})

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'home/home.html', {})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)



    # def get(self, request):
    #     form = Form.HomeForm()
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request):
    #     form = Form.HomeForm(request.POST)
    #     if form.is_valid():
    #         text = form.cleaned_data['post']
    #         form = Form.HomeForm()
    #
    #     args = {'form': form, 'text': text}
    #     return render(request, self.template_name, args)


class Descriptiva_InfoView(TemplateView):
    def __init__(self):
        self.lista_num = "0"

    template_name = 'home/descriptiva_info.html'


    def get(self, request):
        form = Form.Descriptiva_Info()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Descriptiva_Info(request.POST)

        if form.is_valid():
            lista_num = form.cleaned_data['lista_num']
            Descriptiva_InfoView.lista_num = lista_num
            resultado = calcu.descriptiva_info(lista=lista_num)
            form = Form.Descriptiva_Info()

            args = {'form': form, 'resultado': resultado}
            print(lista_num)
            return render(request, self.template_name, args)

        else:
            print("formulario no valido")
            args = {'form': form}
            return render(request, self.template_name, args)



class PoissonView(TemplateView):
    template_name = 'home/poisson.html'

    def get(self, request):
        form = Form.Poisson()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Poisson(request.POST)
        if form.is_valid():
            k = form.cleaned_data['k']
            #Calcula Lambda y lo envia por parametro
            mu = form.cleaned_data['n'] * form.cleaned_data['p']
            resultado = calcu.poisson(k=k, mu=mu)
            form = Form.Poisson()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)

class Poisson_RangoView(TemplateView):
    template_name = 'home/poisson_rango.html'

    def get(self, request):
        form = Form.Poisson_Rango()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Poisson_Rango(request.POST)
        if form.is_valid():
            #Calcula Lambda y lo envia por parametro
            mu = form.cleaned_data['n'] * form.cleaned_data['p']
            inicio = form.cleaned_data['inicio']
            fin = form.cleaned_data['fin']
            resultado = calcu.poisson(mu=mu, inicio=inicio, fin=fin)
            form = Form.Poisson_Rango()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)

class BinomialView(TemplateView):
    template_name = 'home/binomial.html'

    def get(self, request):
        form = Form.Binomial()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Binomial(request.POST)
        if form.is_valid():
            num = form.cleaned_data['n']
            probab = form.cleaned_data['p']
            x_exitos = form.cleaned_data['x']
            resultado = calcu.binomial(n=num, p=probab,  x=x_exitos)
            form = Form.Binomial()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)

class Binomial_RangoView(TemplateView):
    template_name = 'home/binomial_rango.html'

    def get(self, request):
        form = Form.Binomial_Rango()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Binomial_Rango(request.POST)
        if form.is_valid():
            num = form.cleaned_data['n']
            probab = form.cleaned_data['p']
            inicio = form.cleaned_data['inicio']
            fin = form.cleaned_data['fin']
            resultado = calcu.binomial_rango(n=num, p=probab, inicio=inicio, fin=fin)
            form = Form.Binomial_Rango()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)

class Estimacion_ProporcionView(TemplateView):
    template_name = 'home/estimacion_proporcion.html'

    def get(self, request):
        form = Form.Estimacion_Proporcion()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Estimacion_Proporcion(request.POST)
        if form.is_valid():
            num = form.cleaned_data['n']
            probab = form.cleaned_data['p']
            confi = form.cleaned_data['confianza']
            resultado = calcu.intervalo_confianza_proporcion(n=num, p=probab, confianza=confi)
            form = Form.Estimacion_Proporcion()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)


class Estimacion_MediaView(TemplateView):
    def __init__(self):
        self.media = 0
    template_name = 'home/estimacion_media.html'

    def get(self, request):
        form = Form.Estimacion_Media()
        form_modal = Form.Descriptiva_Info()
        args = {'form': form, 'form_modal': form_modal}
        return render(request, self.template_name, args)

    def post(self, request):
        form = Form.Estimacion_Media(request.POST)
        form_modal = Form.Descriptiva_Info(request.POST)
        resultado = None
        lista_num = '0'

        if form.is_valid():
            n = form.cleaned_data['n']
            std = form.cleaned_data['std']
            x = form.cleaned_data['x']
            confi = form.cleaned_data['confianza']
            resultado = calcu.intervalo_confianza_media(n=n, std=std, x=x, confianza=confi)

            form = Form.Estimacion_Media()
            form_modal = Form.Descriptiva_Info()

            args = {'form': form, 'form_modal': form_modal, 'resultado': resultado, }
            return render(request, self.template_name, args)


        #para el post del MODAL
        if form_modal.is_valid():
            #proceso para obtener los resultados de la lista
            lista_num = form_modal.cleaned_data['lista_num']
            Descriptiva_InfoView.lista_num = lista_num
            resultado_descriptiva = calcu.descriptiva_info(lista=lista_num)
            #guardamos los valores en variables
            media = resultado_descriptiva['media']
            desviacion_estandar = resultado_descriptiva['std']
            tamano = resultado_descriptiva['tamano']
            #limpiamos el modal
            form_modal = Form.Descriptiva_Info()

            #creamos el formulario con los valores obtenidos de la lista
            class Estimacion_Media(forms.Form):

                    n = forms.IntegerField(min_value=1, label='N',initial=tamano,
                                                widget=forms.NumberInput(
                                                    attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese tamaño de muestra, ejemplo 30'})
                                            )
                    std = forms.FloatField(min_value=0, label='σ',initial=desviacion_estandar,
                                        widget=forms.NumberInput(
                                            attrs={'class': 'form-control',
                                            'placeholder': 'Ingrese Desviación Estandar'})
                                        )
                    x = forms.FloatField(min_value=0, label='X', initial=media,
                                        widget=forms.NumberInput(
                                            attrs={'class': 'form-control',
                                            'placeholder': 'Ingrese la media (promedio)'})
                                        )

                    confianza = forms.FloatField(min_value=0, max_value=100, label='Confianza',
                                        widget=forms.NumberInput(
                                            attrs={'class': 'form-control',
                                            'placeholder': 'Ingrese % confianza, ejemplo 95'})
                                        )

            #llamamos el form con los valores ya establecidos
            form = Estimacion_Media()
            args = {'form': form, 'form_modal': form_modal}
            return render(request, self.template_name, args)

        else:
            #no limpiamos el modal para que revise el error
            #form_modal = Form.Descriptiva_Info()
            form = Form.Estimacion_Media()
            error = True
            args = {'form': form, 'form_modal': form_modal, 'error':error}
            return render(request, self.template_name, args)



        #args = {'form': form, 'form_modal': form_modal, 'resultado': resultado,}
        #return render(request, self.template_name, args)

class TStudentView(TemplateView):
    template_name = 'home/tstudent.html'

    def get(self, request):
        form = Form.TStudent()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.TStudent(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            t_score1 = form.cleaned_data['t_score1']
            t_score2 = form.cleaned_data['t_score2']
            resultado = calcu.t_student(n, t_score1, t_score2)
            form = Form.TStudent()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)
