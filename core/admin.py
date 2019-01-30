from django.contrib import admin
from .models import Despesa


admin.site.register(Despesa)



#default:"Administração do Django"
admin.site.site_header='Painel de Controle'

#default:"Administração do Site"
admin.site.index_title='Recursos'

#default:"Site de Administração do Django"
admin.site.site_title='Titulo HTML do Site'

