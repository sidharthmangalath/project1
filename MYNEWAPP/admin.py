from django.contrib import admin
from .models import customer
from .models import StudentData
from .models import PlayerDetails
from .models import Student5
admin.site.register(customer)
# Register your models here.
admin.site.register(StudentData)
admin.site.register(PlayerDetails)
admin.site.register(Student5)