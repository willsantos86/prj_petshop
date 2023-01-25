from django.urls import path

from rest_api.views import  AgendamentoModelViewSet, ContatoModelViewSet

from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('contatos', ContatoModelViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls