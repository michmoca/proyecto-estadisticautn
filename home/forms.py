from django import forms

class HomeForm(forms.Form):
    post = forms.CharField()


class descriptiva_info(forms.Form):
    lista_num = forms.IntegerField(label='Ingrese la lista de números separados por comas',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo: 10, 54, 36, 12.5, 8'})
                            )

class TStudent(forms.Form):
    n = forms.IntegerField(label='N',
                            #help_text='Grados de libertad',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Grados de Libertad'}),
                            )
    t_score1 = forms.FloatField(label='T-Score 1',
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control',
                                        'placeholder': 'T-Score 1'}),
                                )
    t_score2 = forms.FloatField(label='T-Score 2', required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'T-Score 2'}),
                                )


class Estimacion(forms.Form):
    n = forms.IntegerField(label='N',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ingrese numero, ejemplo 300'})
                            )
    p = forms.FloatField(label='P',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese probabilidad, ejemplo 0.20'})
                        )
    confianza = forms.FloatField(label='Confianza',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ingrese % confianza, ejemplo 95'})
                        )

class Binomial(forms.Form):
    x = forms.IntegerField(label='x: Ingrese número de éxitos observados',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 13'})
                            )
    n = forms.IntegerField(label='n: Ingrese número de ensayos',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 15'})
                        )
    p = forms.FloatField(label='p: Probabilidad de éxito en cada ensayo',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.72'})
                        )

class Binomial_Rango(forms.Form):
    n = forms.IntegerField(label='n: Ingrese número de ensayos',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 4'})
                        )
    p = forms.FloatField(label='p: Probabilidad de éxito.',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.9'})
                        )
    inicio = forms.IntegerField(label='Ingrese el número inicial del rango',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 1'})
                            )
    fin = forms.IntegerField(label='Ingrese el número final del rango',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 3'})
                        )

class Poisson(forms.Form):
    k = forms.IntegerField(label='k: Ingrese número de fracasos',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 4'})
                            )
    # mu = forms.IntegerField(label='Lambda: es el producto de n*p',
    #                     widget=forms.TextInput(
    #                         attrs={'class': 'form-control',
    #                         'placeholder': 'Ejemplo 3'})
    #                     )

    n = forms.IntegerField(label='Ingrese el número de ensayos',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 100'})
                        )

    p = forms.FloatField(label='Ingrese la probabilidad',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.03'})
                        )


class Poisson_Rango(forms.Form):
    # mu = forms.IntegerField(label='Lambda: es el producto de n*p',
    #                     widget=forms.TextInput(
    #                         attrs={'class': 'form-control',
    #                         'placeholder': 'Ejemplo 3'})
    #                     )

    n = forms.IntegerField(label='Ingrese el número de ensayos',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 100'})
                        )

    p = forms.FloatField(label='Ingrese la probabilidad',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 0.03'})
                        )

    inicio = forms.IntegerField(label='Ingrese el número inicial del rango',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Ejemplo 1'})
                            )
    fin = forms.IntegerField(label='Ingrese el número final del rango',
                        widget=forms.TextInput(
                            attrs={'class': 'form-control',
                            'placeholder': 'Ejemplo 3'})
                        )
