from django.contrib import admin
from . models import patientRegistrationDatas,doctorData,patientRecord,adminRegistrations,departmentData,settingspage,appointmentspage,doctorSchedule,employeeAdd,leaveData,holidayData
# Register your models here.

admin.site.register(patientRegistrationDatas)
admin.site.register(doctorData)
admin.site.register(patientRecord)
admin.site.register(adminRegistrations)
admin.site.register(departmentData)
admin.site.register(settingspage)
admin.site.register(appointmentspage)
admin.site.register(doctorSchedule)
admin.site.register(employeeAdd)
admin.site.register(leaveData)
admin.site.register(holidayData)

