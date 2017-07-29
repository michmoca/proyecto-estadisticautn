from django.views.generic import TemplateView
from django.shortcuts import render
from home import forms as Form
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
    template_name = 'home/descriptiva_info.html'
    def __init__(self):
        self.lista_num = "0"

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

class EstimacionView(TemplateView):
    template_name = 'home/estimacion.html'

    def get(self, request):
        form = Form.Estimacion()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.Estimacion(request.POST)
        if form.is_valid():
            num = form.cleaned_data['n']
            probab = form.cleaned_data['p']
            confi = form.cleaned_data['confianza']
            resultado = calcu.intervalo_confianza_proporcion(n=num, p=probab, confianza=confi)
            form = Form.Estimacion()

        args = {'form': form, 'resultado': resultado}
        return render(request, self.template_name, args)

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
