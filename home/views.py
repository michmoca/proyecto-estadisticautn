from django.views.generic import TemplateView
from django.shortcuts import render
from home import forms as Form
from home import calculations as calcu


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = Form.HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form.HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = Form.HomeForm()

        args = {'form': form, 'text': text}
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
