from django.conf.urls import url
from home import views
from home import charts

urlpatterns = [
    url(r'^chi-cuadrada/$', views.Chi_CuadradaView.as_view(), name='chi_cuadrada'),
    url(r'^calculadora1/$', views.Calculadora1View.as_view(), name='calculadora1'),
    url(r'^calculadora2/$', views.Calculadora2View.as_view(), name='calculadora2'),
    url(r'^charts/boxplot.jpg$', charts.boxplot),
    url(r'^charts/histograma.png$', charts.histograma),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.CharData.as_view()),
    url(r'^tstudent/$', views.TStudentView.as_view(), name='tstudent'),
    url(r'^hipotesis-diferencia-medias/$', views.Hipotesis_Diferencia_MediasView.as_view(), name='hipotesis_diferencia_medias'),
    url(r'^hipotesis-media/$', views.Hipotesis_MediaView.as_view(), name='hipotesis_media'),
    url(r'^hipotesis-proporcion/$', views.Hipotesis_ProporcionView.as_view(), name='hipotesis_proporcion'),
    url(r'^estimacion-proporcion/$', views.Estimacion_ProporcionView.as_view(), name='estimacion'),
    url(r'^estimacion-media/$', views.Estimacion_MediaView.as_view(), name='estimacion_media'),
    url(r'^binomial/$', views.BinomialView.as_view(), name='binomial'),
    url(r'^binomial-rango/$', views.Binomial_RangoView.as_view(), name='binomial_rango'),
    url(r'^poisson/$', views.PoissonView.as_view(), name='poisson'),
    url(r'^poisson-rango/$', views.Poisson_RangoView.as_view(), name='poisson_rango'),
    url(r'^descriptiva-info/$', views.Descriptiva_InfoView.as_view(), name='descriptiva-info'),
    url(r'^contacto/$', views.ContactoView.as_view(), name='contacto'),
]
