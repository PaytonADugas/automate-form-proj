from django.conf.urls import url
from form_app import views

app_name = 'form_app'

urlpatterns = [
    url('form', views.form, name='form'),
    url('display', views.display, name='display'),
    url('student/(?P<slug>[\w-]+)$', views.student, name='student'),
]
