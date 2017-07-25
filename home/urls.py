from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^tstudent/$', views.TStudentView.as_view(), name='tstudent'),
    url(r'^estimacion/$', views.EstimacionView.as_view(), name='estimacion'),
    url(r'^binomial/$', views.BinomialView.as_view(), name='binomial'),
    url(r'^binomial-rango/$', views.Binomial_RangoView.as_view(), name='binomial_rango'),
    url(r'^poisson/$', views.PoissonView.as_view(), name='poisson'),
    url(r'^poisson-rango/$', views.Poisson_RangoView.as_view(), name='poisson_rango'),
    url(r'^descriptiva-info/$', views.Descriptiva_InfoView.as_view(), name='descriptiva-info'),
    url(r'^contacto/$', views.ContactoView.as_view(), name='contacto'),
]
