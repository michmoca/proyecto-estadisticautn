from django import forms
from django.core import validators



class HomeForm(forms.Form):
    pass

class Contacto(forms.Form):
    subject = forms.CharField(label='Asunto',
                            #help_text='Grados de libertad',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Asunto '}),
                            )
    message = forms.CharField(label='Mensaje',
                                    widget=forms.Textarea(
                                        attrs={'class': 'form-control',
                                        'placeholder': 'Mensaje'}),
                                )
    from_email = forms.CharField(label='Tu correo',
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'correo'}),
                                )

class Descriptiva_Info(forms.Form):
    lista_num = forms.CharField(validators=[validators.int_list_validator(sep=',', message='Formato invalido'),],
                                label='Ingrese la lista de números separados por comas',
                                widget=forms.Textarea(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo: 10, 54, 36, 12.5, 8'}),

                            )

class TStudent(forms.Form):
    n = forms.IntegerField(min_value=1, max_value=30,
                                label='N: Grados de libertad',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo: 20'}),

                            )
    t_score1 = forms.FloatField(label='T-Score 1',
                                    widget=forms.NumberInput(
                                        attrs={'class': 'form-control',
                                        'placeholder': 'Ejemplo: 2.861'}),
                                )
    t_score2 = forms.FloatField(label='T-Score 2', required=False,
                                #help_text='Ver video minuto 2 para ejemplo.',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Opcional  '}),
                                )

class Estimacion_Proporcion(forms.Form):
    n = forms.IntegerField(min_value=1, label='N',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ingrese numero, ejemplo 300'})
                            )
    p = forms.FloatField(min_value=0, max_value=1, label='P',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese probabilidad, ejemplo 0.20'})
                        )
    confianza = forms.FloatField(min_value=0, max_value=100, label='Confianza',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese % confianza, ejemplo 95'})
                        )

class Estimacion_Media(forms.Form):

    x = forms.FloatField(min_value=0, label='X',
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control',
                                'placeholder': 'Ingrese la media (promedio)'})
                            )

    n = forms.IntegerField(min_value=1, label='N',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ingrese tamaño de muestra, ejemplo 30'})
                            )
    std = forms.FloatField(min_value=0, label='σ',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese Desviación Estandar'})
                        )



    confianza = forms.FloatField(min_value=0, max_value=100, label='Confianza',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese % confianza, ejemplo 95'})
                        )

class Binomial(forms.Form):
    x = forms.IntegerField(min_value=1, label='x: Ingrese número de éxitos observados',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 13'})
                            )
    n = forms.IntegerField(min_value=1, label='n: Ingrese número de ensayos',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 15'})
                        )
    p = forms.FloatField(min_value=0, max_value=1, label='p: Probabilidad de éxito en cada ensayo',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.72'})
                        )

class Binomial_Rango(forms.Form):
    n = forms.IntegerField(min_value=1, label='n: Ingrese número de ensayos',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 4'})
                        )
    p = forms.FloatField(min_value=0, max_value=1, label='p: Probabilidad de éxito.',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.9'})
                        )
    inicio = forms.IntegerField(min_value=0, label='Ingrese el número inicial del rango',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 1'})
                            )
    fin = forms.IntegerField(min_value=1, label='Ingrese el número final del rango',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 3'})
                        )

class Poisson(forms.Form):
    k = forms.IntegerField(min_value=1, label='k: Ingrese número de fracasos',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 4'})
                            )
    # mu = forms.IntegerField(label='Lambda: es el producto de n*p',
    #                     widget=forms.TextInput(
    #                         attrs={'class': 'form-control',
    #                         'placeholder': 'Ejemplo 3'})
    #                     )

    n = forms.IntegerField(min_value=1, label='Ingrese el número de ensayos',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 100'})
                        )

    p = forms.FloatField(min_value=0, max_value=1, label='Ingrese la probabilidad',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.03'})
                        )


class Poisson_Rango(forms.Form):
    # mu = forms.IntegerField(label='Lambda: es el producto de n*p',
    #                     widget=forms.TextInput(
    #                         attrs={'class': 'form-control',
    #                         'placeholder': 'Ejemplo 3'})
    #                     )

    n = forms.IntegerField(min_value=1, label='Ingrese el número de ensayos',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 100'})
                        )

    p = forms.FloatField(min_value=0, max_value=1, label='Ingrese la probabilidad',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.03'})
                        )

    inicio = forms.IntegerField(min_value=0, label='Ingrese el número inicial del rango',
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 1'})
                            )
    fin = forms.IntegerField(min_value=1, label='Ingrese el número final del rango',
                        widget=forms.NumberInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 3'})
                        )
