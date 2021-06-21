from django.contrib import admin
from endpoints.models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest, ABTest 

# Register your models here.
admin.site.register(Endpoint)
admin.site.register(MLAlgorithm)
admin.site.register(MLAlgorithmStatus)
admin.site.register(MLRequest)
admin.site.register(ABTest)