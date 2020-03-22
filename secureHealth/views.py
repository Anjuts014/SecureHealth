from django.shortcuts import render
from django .http import HttpResponse
from django.http import HttpResponseRedirect
from . forms import registerForm ,doctorDataForm,patientRecordForm,adminRegistrationForm,settingsForm,appointmentForm,doctorScheduleForm,departmentForm,employeeForm,leaveForm,holidayForm
from . models import patientRegistrationDatas, doctorData,patientRecord, adminRegistrations,settingspage,appointmentspage,doctorSchedule,departmentData,employeeAdd,leaveData,holidayData
from django.contrib.auth.models import User
from django.core.mail.message import EmailMessage
from datetime import datetime
from secureHealth.sh_encryption import enc_decr


def home(request):
    return HttpResponse("hello")

def indexpage(request):
    return render(request,'secureHealth/index.html')

def basepage(request):
    return render(request,'secureHealth/base.html')

def activitiespage(request):
    return render(request,'secureHealth/activities.html')

def addasset(request):
    return render(request,'secureHealth/add-asset.html')

def addblog(request):
    return render(request,'secureHealth/add-blog.html')

def adminregistration(request):
    if request.method == "POST":
        form = adminRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']
            from_email='ecommercedvlpr@gmail.com'

            adminReg= adminRegistrations()

            adminReg.username = username
            adminReg.email = email
            adminReg.mobile_number=mobile_number
            adminReg.password= password
            adminReg.save()
            mail = EmailMessage("Admin Registration Verification","To confirm the admin request,details have been sent to the respective Hospital to verify the information.After that admin can login",from_email,[email])
            mail.send()
            return HttpResponse("form submitted")
    else:
        form = adminRegistrations()
   
    return render(request,'secureHealth/register.html',{'form':form})
    

def doctors(request):
    hospital = request.session['hospital']
    doctor_details = doctorData.objects.filter(hospital_name=hospital)
    return render(request,'secureHealth/doctors.html',{'doctors':doctor_details,'role':'admin'})

def doctorpages(request):
    doctor_details = doctorData.objects.all()
    return render(request,'secureHealth/doctors-1.html',{'doctors':doctor_details,'role':'doctor'})

def editdoctor(request,id):
    doctor = doctorData.objects.get(id = id)
    date_of_birth = doctor.date_of_birth
    date_of_birth = date_of_birth.strftime("%Y-%m-%d")
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_Password = request.POST['confirm_Password']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        gender = request.POST['gender']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        district = request.POST['district']
        pincode = request.POST['pincode']
        mobile_number = request.POST['mobile_number']
        phone_number = request.POST['phone_number']
        status = request.POST['status']
        short_biography = request.POST['short_biography']

        doctor.first_name = first_name
        doctor.last_name = last_name
        doctor.username = username
        doctor.email = email
        doctor.password = password
        doctor.confirm_Password = confirm_Password
        doctor.date_of_birth = date_of_birth
        doctor.address = address
        doctor.gender = gender
        doctor.country = country
        doctor.city= city
        doctor.state = state
        doctor.district = district
        doctor.pincode = pincode
        doctor.status = status
        doctor.mobile_number = mobile_number
        doctor.phone_number = phone_number
        doctor.short_biography = short_biography

        doctor.save()
        return HttpResponse("successfully updated doctor") 

    return render(request,'secureHealth/edit-doctor.html',{'doctor':doctor,'date_of_birth':date_of_birth,'role':'admin'})

def deletedoctor(request,id):
    doctor = doctorData.objects.get(id = id)
    doctor.delete()
    doctor_details = doctorData.objects.all()
    return render(request,'secureHealth/doctors.html',{'doctors':doctor_details,'role':'admin'})

def profileDoctor(request):
    return render(request,'secureHealth/profile.html')

def editprofile(request):
    return render(request,'secureHealth/edit-profile.html')

def adddoctor(request):
    form = doctorDataForm()
    if request.method == "POST":
        form = doctorDataForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_Password = form.cleaned_data['confirm_Password']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            photo = form.cleaned_data['photo']
            pincode = form.cleaned_data['pincode']
            mobile_number = form.cleaned_data['mobile_number']
            phone_number = form.cleaned_data['phone_number']
            status = form.cleaned_data['status']
            short_biography = form.cleaned_data['short_biography']

            drData = doctorData()

            drData.first_name = first_name
            drData.last_name = last_name
            drData.username = username
            drData.email = email
            drData.password = password
            drData.confirm_Password = confirm_Password
            drData.date_of_birth = date_of_birth
            drData.address = address
            drData.gender = gender
            drData.country = country
            drData.city= city
            drData.state = state
            drData.district = district
            drData.photo = photo
            drData.pincode = pincode
            drData.status = status
            drData.mobile_number = mobile_number
            drData.phone_number = phone_number
            drData.short_biography = short_biography

            drData.save()

            return HttpResponse("successfully saved details of doctor")
        else:
            print(form.errors)

    return render(request,'secureHealth/add-doctor.html', {'form':form})

def adminIndex(request):
    return render(request,'secureHealth/admin-index.html')

def adminIndex2(request):
    patient_details = patientRegistrationDatas.objects.all()[:3]
    doctor_details = doctorData.objects.all()[:3]
    appointment_details = appointmentspage.objects.all()[:3]
    return render(request,'secureHealth/index-2.html',{'patients':patient_details,'doctors':doctor_details,'appointments':appointment_details,'role':'admin'})

def patientdetails(request):
    # hospital = request.session['hospital']
    # patient_details = patientRegistrationDatas.objects.filter(hospital_name=hospital)
    patient_details = patientRegistrationDatas.objects.all()
    patient_data = []
    for patient_info in patient_details:
        first_name = enc_decr.decrypt(patient_info.first_name)
        last_name = enc_decr.decrypt(patient_info.last_name)
        email = enc_decr.decrypt(patient_info.email)
        date_of_birth = patient_info.date_of_birth
        blood_group = enc_decr.decrypt(patient_info.blood_group)
        gender = enc_decr.decrypt(patient_info.gender)
        country = enc_decr.decrypt(patient_info.country)
        city = enc_decr.decrypt(patient_info.city)
        state = enc_decr.decrypt(patient_info.state)
        district = enc_decr.decrypt(patient_info.district)
        pincode = enc_decr.decrypt(patient_info.pincode)
        mobile_number = enc_decr.decrypt(patient_info.mobile_number)
        status= enc_decr.decrypt(patient_info.status)
        decrypt_patient_details = {'id':patient_info.id,'first_name':first_name,'last_name':last_name,'date_of_birth':date_of_birth,'blood_group':blood_group,'gender':gender,'country':country,'city':city,'state':state,'district':district,'pincode':pincode,'mobile_number':mobile_number,'status':status}
        patient_data.append(decrypt_patient_details)
    return render(request,'secureHealth/patients.html',{'patients':patient_data,'role':'admin'})


def patientinfo(request):
    patient_details = patientRegistrationDatas.objects.all()
    return render(request,'secureHealth/patient-1.html',{'patients':patient_details,'role':'doctor'})

def addPatient(request):
    form = registerForm()
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_Password = form.cleaned_data['confirm_Password']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            pincode = form.cleaned_data['pincode']
            mobile_number = form.cleaned_data['mobile_number']
            status = form.cleaned_data['status']

            pRD = patientRegistrationDatas()

            pRD.first_name = enc_decr.encrypt(first_name)
            pRD.last_name = enc_decr.encrypt(last_name)
            pRD.username = enc_decr.encrypt(username)
            pRD.email = enc_decr.encrypt(email)
            pRD.password= enc_decr.encrypt(password)
            pRD.confirm_Password = enc_decr.encrypt(confirm_Password)
            pRD.date_of_birth = date_of_birth
            pRD.address = enc_decr.encrypt(address)
            pRD.blood_group = enc_decr.encrypt(blood_group)
            pRD.gender = enc_decr.encrypt(gender)
            pRD.country = enc_decr.encrypt(country)
            pRD.city = enc_decr.encrypt(city)
            pRD.state = enc_decr.encrypt(state)
            pRD.district = enc_decr.encrypt(district)
            pRD.pincode = enc_decr.encrypt(pincode)
            pRD.mobile_number = enc_decr.encrypt(mobile_number)
            pRD.status= enc_decr.encrypt(status)

            pRD.save()
            return HttpResponse("Registration form is submitted successfully")

    return render(request,'secureHealth/add-patient.html',{'form':form,'role':'admin'})

def editPatient(request,id):
    patient_detail = patientRegistrationDatas.objects.get(id=id)
    first_name = enc_decr.decrypt(patient_detail.first_name)
    last_name = enc_decr.decrypt(patient_detail.last_name)
    username = enc_decr.decrypt(patient_detail.username)
    email = enc_decr.decrypt(patient_detail.email)
    password= enc_decr.decrypt(patient_detail.password)
    confirm_Password = enc_decr.decrypt(patient_detail.confirm_Password)
    address = enc_decr.decrypt(patient_detail.address)
    blood_group = enc_decr.decrypt(patient_detail.blood_group)
    gender = enc_decr.decrypt(patient_detail.gender)
    country = enc_decr.decrypt(patient_detail.country)
    city = enc_decr.decrypt(patient_detail.city)
    state = enc_decr.decrypt(patient_detail.state)
    district = enc_decr.decrypt(patient_detail.district)
    pincode = enc_decr.decrypt(patient_detail.pincode)
    mobile_number = enc_decr.decrypt(patient_detail.mobile_number)
    status= enc_decr.decrypt(patient_detail.status)
    decrypt_info = [first_name,last_name,username,email,password,confirm_Password,address,blood_group,gender,country,city,state,district,pincode,mobile_number,status]
    date_of_birth = patient_detail.date_of_birth
    date_of_birth = date_of_birth.strftime("%Y-%m-%d")
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_Password = request.POST['confirm_Password']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        gender = request.POST['gender']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        district = request.POST['district']
        pincode = request.POST['pincode']
        mobile_number = request.POST['mobile_number']
        status = request.POST['status']

        patient_detail = patientRegistrationDatas.objects.get(id=id)

        patient_detail.first_name = enc_decr.encrypt(first_name)
        patient_detail.last_name = enc_decr.encrypt(last_name)
        patient_detail.username = enc_decr.encrypt(username)
        patient_detail.email = enc_decr.encrypt(email)
        patient_detail.password= enc_decr.encrypt(password)
        patient_detail.confirm_Password = enc_decr.encrypt(confirm_Password)
        patient_detail.date_of_birth = date_of_birth
        patient_detail.address = enc_decr.encrypt(address)
        patient_detail.blood_group = enc_decr.encrypt(blood_group)
        patient_detail.gender = enc_decr.encrypt(gender)
        patient_detail.country = enc_decr.encrypt(country)
        patient_detail.city = enc_decr.encrypt(city)
        patient_detail.state = enc_decr.encrypt(state)
        patient_detail.district = enc_decr.encrypt(district)
        patient_detail.pincode = enc_decr.encrypt(pincode)
        patient_detail.mobile_number = enc_decr.encrypt(mobile_number)
        patient_detail.status= enc_decr.encrypt(status)

        patient_detail.save()
        return HttpResponse("Updated Patient Registration form successfully")

    return render(request,'secureHealth/edit-patient.html',{'patient_detail':patient_detail,'date_of_birth':date_of_birth,'role':'admin','decrypt_info':decrypt_info})

def viewpatient(request,id):
    patient_detail = patientRegistrationDatas.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_Password = request.POST['confirm_Password']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        gender = request.POST['gender']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        district = request.POST['district']
        pincode = request.POST['pincode']
        mobile_number = request.POST['mobile_number']
        status = request.POST['status']

        patient_detail.first_name = first_name
        patient_detail.last_name = last_name
        patient_detail.username = username
        patient_detail.email = email
        patient_detail.password= password
        patient_detail.confirm_Password = confirm_Password
        patient_detail.date_of_birth = date_of_birth
        patient_detail.address = address
        patient_detail.blood_group = blood_group
        patient_detail.gender = gender
        patient_detail.country = country
        patient_detail.city = city
        patient_detail.state = state
        patient_detail.district = district
        patient_detail.pincode = pincode
        patient_detail.mobile_number = mobile_number
        patient_detail.status= status
    return render(request,'secureHealth/view-1.html',{'patient_detail':patient_detail,'role':'doctor'})


def deletepatient(request,id):
    patient = patientRegistrationDatas.objects.get(id=id)
    patient.delete()
    patient_details = patientRegistrationDatas.objects.all()
    return render(request,'secureHealth/patients.html',{'patients':patient_details})

def addAppointment(request):
    form = appointmentForm()
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            patient_name = form.cleaned_data['patient_name']
            appointment_id = form.cleaned_data['appointment_id']
            department = form.cleaned_data['department']
            doctor = form.cleaned_data['doctor']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            patient_phone_number = form.cleaned_data['patient_phone_number']
            patient_email = form.cleaned_data['patient_email']
            message = form.cleaned_data['message']
            appointment_status = form.cleaned_data['appointment_status']
        
            appointments = appointmentspage()

            appointments.patient_name = patient_name
            appointments.appointment_id = appointment_id
            appointments.department = department
            appointments.doctor = doctor
            appointments.date = date
            appointments.time = time
            appointments.patient_phone_number = patient_phone_number
            appointments.patient_email = patient_email
            appointments.message = message
            appointments.appointment_status = appointment_status
            appointments.save()
            return HttpResponse("Appointment submitted successfully")

    return render(request,'secureHealth/add-appointment.html',{'form':form})

def appointment(request):
    appointment_details = appointmentspage.objects.all()
    return render(request,'secureHealth/appointments.html',{'appointments': appointment_details,'role':'admin'})

def editappointment(request,id):
    appointment_data = appointmentspage.objects.get(id=id)
    date = appointment_data.date
    date = date.strftime("%Y-%m-%d")
    time = appointment_data.time
    time = time.strftime("%H:%M:%S")
    if request.method == "POST":
        patient_name = request.POST['patient_name']
        appointment_id = request.POST['appointment_id']
        department = request.POST['department']
        doctor = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        patient_phone_number = request.POST['patient_phone_number']
        patient_email = request.POST['patient_email']
        message = request.POST['message']
        appointment_status = request.POST['appointment_status']
        
        appointment_data.patient_name = patient_name
        appointment_data.appointment_id = appointment_id
        appointment_data.department = department
        appointment_data.doctor = doctor
        appointment_data.date = date
        appointment_data.time = time
        appointment_data.patient_phone_number = patient_phone_number
        appointment_data.patient_email = patient_email
        appointment_data.message = message
        appointment_data.appointment_status = appointment_status
        appointment_data.save()
        return HttpResponse("Appointments updated successfully")

    return render(request,'secureHealth/edit-appointment.html',{'appointment_data':appointment_data,'date':date,'time':time,'role':'admin'})

def deleteappointment(request,id):
    appointment_data = appointmentspage.objects.get(id=id)
    appointment_data.delete()
    appointment_details = appointmentspage.objects.all()
    return render(request,'secureHealth/appointments.html',{'appointments': appointment_details})

def schedule(request):
    schedule_details = doctorSchedule.objects.all()
    return render(request,'secureHealth/schedule.html',{'schedule_assigned':schedule_details,'role':'admin'})

def addschedule(request):
    form = doctorScheduleForm()
    if request.method == "POST":
        form = doctorScheduleForm(request.POST)
        if form.is_valid():
            doctor_name = form.cleaned_data['doctor_name']
            available_days = form.cleaned_data['available_days']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            message = form.cleaned_data['message']
            schedule_status = form.cleaned_data['schedule_status']
    
            doctorScheduledata = doctorSchedule()

            doctorScheduledata.doctor_name = doctor_name
            doctorScheduledata.available_days = available_days
            doctorScheduledata.start_time = start_time
            doctorScheduledata.end_time = end_time
            doctorScheduledata.message = message
            doctorScheduledata.schedule_status = schedule_status
            doctorScheduledata.save()
            return HttpResponse("Doctor schedule have been successfully added")
    return render(request,'secureHealth/add-schedule.html',{'form':form,'role':'admin'})

def editschedule(request,id):
    schedule_data = doctorSchedule.objects.get(id=id)
    start_time = schedule_data.start_time
    start_time = start_time.strftime("%H:%M:%S")
    end_time = schedule_data.end_time
    end_time = end_time.strftime("%H:%M:%S")
    if request.method == "POST":
        doctor_name = request.POST['doctor_name']
        available_days = request.POST['available_days']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        message = request.POST['message']
        schedule_status = request.POST['schedule_status']
    

        schedule_data.doctor_name = doctor_name
        schedule_data.available_days = available_days
        schedule_data.start_time = start_time
        schedule_data.end_time = end_time
        schedule_data.message = message
        schedule_data.schedule_status = schedule_status
        schedule_data.save()
        return HttpResponse("Doctor schedule updated successfully ")

    return render(request,'secureHealth/edit-schedule.html',{'schedule_data':schedule_data,'start_time':start_time,'end_time':end_time,'role':'admin'})


def deleteschedule(request,id):
    schedule_data = doctorSchedule.objects.get(id=id)
    schedule_data.delete()
    schedule_details = doctorSchedule.objects.all()
    return render(request,'secureHealth/schedule.html',{'schedule_assigned':schedule_details})

def departments(request):
    department_details = departmentData.objects.all()
    return render(request,'secureHealth/departments.html',{'departments':department_details,'role':'admin'})

def adddepartment(request):
    form = departmentForm()
    if request.method == "POST":
        form = departmentForm(request.POST)
        if form.is_valid():
            department_name = form.cleaned_data['department_name']
            message = form.cleaned_data['message']
            status = form.cleaned_data['status']
    
            departmentAdded = departmentData()

            departmentAdded.department_name = department_name
            departmentAdded.message = message
            departmentAdded.status = status
            departmentAdded.save()
            return HttpResponse("Departments are added successfully ")
    return render(request,'secureHealth/add-department.html',{'form':form,'role':'admin'})

def editdepartment(request,id):
    department = departmentData.objects.get(id=id)
    if request.method == "POST":
        department_name = request.POST['department_name']
        message = request.POST['message']
        status = request.POST['status']

        department.department_name = department_name
        department.message = message
        department.status = status
        department.save()
        return HttpResponse("Departments are added successfully ")

    return render(request,'secureHealth/edit-department.html',{'department':department,'role':'admin'})

def deletedepartment(request,id):
    department = departmentData.objects.get(id=id)
    department.delete()
    department_details = departmentData.objects.all()
    return render(request,'secureHealth/departments.html',{'departments':department_details})

def chat(request):
    return render(request,'secureHealth/chat.html')

def employees(request):
    # hospital = request.session['hospital']
    # employee_details = employeeAdd.objects.filter(hospital_name=hospital)
    return render(request,'secureHealth/employees.html',{'employees':employee_details,'role':'admin'})

def addemployee(request):
    form = employeeForm()
    if request.method == "POST":
        form = employeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_Password = form.cleaned_data['confirm_Password']
            employee_id = form.cleaned_data['employee_id']
            joining_date = form.cleaned_data['joining_date']
            phone_number = form.cleaned_data['phone_number']
            role = form.cleaned_data['role']
            status = form.cleaned_data['status']
            
            employeedata = employeeAdd()

            employeedata.first_name = first_name
            employeedata.last_name = last_name
            employeedata.username = username
            employeedata.email = email
            employeedata.password = password
            employeedata.confirm_Password = confirm_Password
            employeedata.employee_id = employee_id
            employeedata.joining_date = joining_date
            employeedata.phone_number = phone_number
            employeedata.role = role
            employeedata.status = status
            employeedata.save()
            return HttpResponse("Employees are added successfully ")
    

    return render(request,'secureHealth/add-employee.html',{'form':form,'role':'admin'})

def editemployee(request,id):
    employee = employeeAdd.objects.get(id = id)
    joining_date = employee.joining_date
    joining_date = joining_date.strftime("%Y-%m-%d")
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_Password = request.POST['confirm_Password']
        employee_id = request.POST['employee_id']
        joining_date = request.POST['joining_date']
        phone_number = request.POST['phone_number']
        role = request.POST['role']
        status = request.POST['status']
        
        employee.first_name = first_name
        employee.last_name = last_name
        employee.username = username
        employee.email = email
        employee.password = password
        employee.confirm_Password = confirm_Password
        employee.employee_id = employee_id
        employee.joining_date = joining_date
        employee.phone_number = phone_number
        employee.role = role
        employee.status = status
        employee.save()
        return HttpResponse("Employees are updated successfully ")

    return render(request,'secureHealth/edit-employee.html',{'employee':employee,'joining_date':joining_date,'role':'admin'})

def deleteemployee(request,id):
    employee = employeeAdd.objects.get(id = id)
    employee.delete()
    employee_details = employeeAdd.objects.all()
    return render(request,'secureHealth/employees.html',{'employees':employee_details})



def leaves(request):
    hospital = request.session['hospital']
    leave_details = leaveData.objects.filter(hospital_name=hospital)
    return render(request,'secureHealth/leaves.html',{'leaves':leave_details,'role':'admin'})

def leaveinfo(request):
    leave_details = leaveData.objects.all()
    return render(request,'secureHealth/leave-1.html',{'leaves':leave_details,'role':'doctor'})

def addleave(request):
    form = leaveForm()
    if request.method == "POST":
        form = leaveForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            employee_role = form.cleaned_data['employee_role']
            leave_type = form.cleaned_data['leave_type']
            leave_from = form.cleaned_data['leave_from']
            leave_to = form.cleaned_data['leave_to']
            number_of_days = form.cleaned_data['number_of_days']
            remaining_leaves = form.cleaned_data['remaining_leaves']
            leave_reason = form.cleaned_data['leave_reason']

            leaveRecord = leaveData()

            leaveRecord.employee_id = employee_id
            leaveRecord.employee_role = employee_role
            leaveRecord.leave_type = leave_type
            leaveRecord.leave_from = leave_from
            leaveRecord.leave_to = leave_to
            leaveRecord.number_of_days = number_of_days
            leaveRecord.remaining_leaves = remaining_leaves
            leaveRecord.leave_reason = leave_reason
            leaveRecord.save()
            return HttpResponse("Leave request sent successfully")

    return render(request,'secureHealth/add-leave.html',{'form':form,'role':'admin'})

def addleaveinfo(request):
    form = leaveForm()
    if request.method == "POST":
        form = leaveForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            employee_role = form.cleaned_data['employee_role']
            leave_type = form.cleaned_data['leave_type']
            leave_from = form.cleaned_data['leave_from']
            leave_to = form.cleaned_data['leave_to']
            number_of_days = form.cleaned_data['number_of_days']
            remaining_leaves = form.cleaned_data['remaining_leaves']
            leave_reason = form.cleaned_data['leave_reason']

            leaveRecord = leaveData()

            leaveRecord.employee_id = employee_id
            leaveRecord.employee_role = employee_role
            leaveRecord.leave_type = leave_type
            leaveRecord.leave_from = leave_from
            leaveRecord.leave_to = leave_to
            leaveRecord.number_of_days = number_of_days
            leaveRecord.remaining_leaves = remaining_leaves
            leaveRecord.leave_reason = leave_reason
            leaveRecord.save()
            return HttpResponse("Leave request sent successfully")

    return render(request,'secureHealth/add-leave-1.html',{'form':form,'role':'doctor'})




def editleave(request,id):
    leave = leaveData.objects.get(id = id)
    leave_from = leave.leave_from
    leave_from = leave_from.strftime("%Y-%m-%d")
    leave_to = leave.leave_to
    leave_to = leave_to.strftime("%Y-%m-%d")
    if request.method == "POST":
        employee_id = request.POST['employee_id']
        employee_role = request.POST['employee_role']
        leave_type = request.POST['leave_type']
        leave_from = request.POST['leave_from']
        leave_to = request.POST['leave_to']
        number_of_days = request.POST['number_of_days']
        remaining_leaves = request.POST['remaining_leaves']
        status = request.POST['status']
        leave_reason = request.POST['leave_reason']

        # leave_from.strftime("%Y-%m-%d")
        # print(leave_from)

        leave.employee_id = employee_id
        leave.employee_role = employee_role
        leave.leave_type = leave_type
        leave.leave_from = leave_from
        leave.leave_to = leave_to
        leave.number_of_days = number_of_days
        leave.remaining_leaves = remaining_leaves
        leave.leave_reason = leave_reason
        leave.status=status
        leave.save()
        return HttpResponse("Leave request updated successfully")

    return render(request,'secureHealth/edit-leave.html',{'leave':leave,'leave_from':leave_from,"leave_to":leave_to,'role':'admin'})

def deleteleave(request,id):
    leave = leaveData.objects.get(id = id)
    leave.delete()
    leave_details = leaveData.objects.all()
    return render(request,'secureHealth/leaves.html',{'leaves':leave_details})

def doctorleave(request):
    form = leaveForm()
    if request.method == "POST":
        form = leaveForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            employee_role = form.cleaned_data['employee_role']
            leave_type = form.cleaned_data['leave_type']
            leave_from = form.cleaned_data['leave_from']
            leave_to = form.cleaned_data['leave_to']
            number_of_days = form.cleaned_data['number_of_days']
            remaining_leaves = form.cleaned_data['remaining_leaves']
            leave_reason = form.cleaned_data['leave_reason']

            leaveRecord = leaveData()

            leaveRecord.employee_id = employee_id
            leaveRecord.employee_role = employee_role
            leaveRecord.leave_type = leave_type
            leaveRecord.leave_from = leave_from
            leaveRecord.leave_to = leave_to
            leaveRecord.number_of_days = number_of_days
            leaveRecord.remaining_leaves = remaining_leaves
            leaveRecord.leave_reason = leave_reason
            leaveRecord.save()
            return HttpResponse("Leave request sent successfully")

    return render(request,'secureHealth/doctorpage-leave.html',{'form':form})

def holidays(request):
    # hospital = request.session['hospital']
    # holiday_details = holidayData.objects.filter(hospital_name=hospital)
    return render(request,'secureHealth/holidays.html',{'holidays':holiday_details,'role':'admin'})

def addholiday(request):
    form = holidayForm()
    if request.method == "POST":
        form = holidayForm(request.POST)
        if form.is_valid():
            holiday_name = form.cleaned_data['holiday_name']
            holiday_day = form.cleaned_data['holiday_day']
            holiday_date = form.cleaned_data['holiday_date']
           
            holidayInfo = holidayData()

            holidayInfo.holiday_name = holiday_name
            holidayInfo.holiday_day = holiday_day
            holidayInfo.holiday_date = holiday_date
            
            holidayInfo.save()
            return HttpResponse("Holiday Infomation successfully added")

    return render(request,'secureHealth/add-holiday.html',{'form':form,'role':'admin'})

def editholiday(request,id):
    holiday = holidayData.objects.get(id = id)
    if request.method == "POST":
        holiday_name = request.POST['holiday_name']
        holiday_day = request.POST['holiday_day']
        holiday_date = request.POST['holiday_date']
        
        holiday.holiday_name = holiday_name
        holiday.holiday_day = holiday_day
        holiday.holiday_date = holiday_date
        
        holiday.save()
        return HttpResponse("Holiday updated successfully")

    return render(request,'secureHealth/edit-holiday.html',{'holiday':holiday})

def deleteholiday(request,id):
    holiday = holidayData.objects.get(id = id)
    holiday.delete()
    holiday_details = holidayData.objects.all()
    return render(request,'secureHealth/holidays.html',{'holidays':holiday_details,'role':'admin'})

def attendance(request):
    return render(request,'secureHealth/attendance.html')


def settings(request):
    form = settingsForm()
    if request.method == "POST":
        form = settingsForm(request.POST)
        if form.is_valid():
            hospital_name = form.cleaned_data['hospital_name']
            contact_person = form.cleaned_data['contact_person']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            mobile_number = form.cleaned_data['mobile_number']
            fax = form.cleaned_data['fax']
            website_url = form.cleaned_data['website_url']

            settings1 = settingspage()

            settings1.hospital_name = hospital_name
            settings1.contact_person = contact_person
            settings1.address = address
            settings1.country = country
            settings1.city = city
            settings1.state = state
            settings1.pincode = pincode
            settings1.email = email
            settings1.phone_number = phone_number
            settings1.mobile_number = mobile_number
            settings1.fax= fax
            settings1.website_url = website_url
            settings1.save()
            return HttpResponse("successfully saved the Hospital details")

    return render(request,'secureHealth/settings.html',{'form':form,'role':'admin'})

def adminlogin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        adminLogin = adminRegistrations.objects.all().filter(username=username, password=password)
        for admin in adminLogin:
            hospital = admin.hospital_name
        
        if adminLogin:
            form = adminRegistrationForm()
            request.session.set_expiry(300)
            request.session['hospital']=hospital
            patient_details = patientRegistrationDatas.objects.filter(hospital_name=hospital)[:3]
            doctor_details = doctorData.objects.filter(hospital_name=hospital)[:3]
            appointment_details = appointmentspage.objects.filter(hospital_name=hospital)[:3]
            return render(request,'secureHealth/index-2.html',{'form':form ,'role':'admin','patients':patient_details,'doctors':doctor_details,'appointments':appointment_details,'role':'admin'})
     
    return render(request,'secureHealth/login.html')


def login(request):
    patient_details = patientRegistrationDatas.objects.all()[:3]
    doctor_details = doctorData.objects.all()[:3]
    appointment_details = appointmentspage.objects.all()[:3]
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        patientLogin = patientRegistrationDatas.objects.all().filter(username=enc_decr.decrypt(username), password=enc_decr.decrypt(password))
        print(enc_decr.decrypt(username))
        if patientLogin:
            form = patientRecordForm()
            request.session['username']=username
            user1 = request.session['username']
            request.session.set_expiry(300)
            return render(request,'secureHealth/index-2.html',{'form':form,'user1':user1,'role':'patient','patients':patient_details,'doctors':doctor_details,'appointments':appointment_details})

    return render(request,'secureHealth/userLoginpage.html')

def forgotPassword(request):
    return render(request,'forgotpassword.html')

def doctorLogin(request):
    patient_details = patientRegistrationDatas.objects.all()[:3]
    doctor_details = doctorData.objects.all()[:3]
    appointment_details = appointmentspage.objects.all()[:3]
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        doctorLogin = doctorData.objects.all().filter(username=username, password=password)
        if doctorLogin:
            request.session['username']=username
            user1 = request.session['username']
            request.session.set_expiry(300)
            return render(request,'secureHealth/index-2.html',{'user1':user1, 'role':'doctor','patients':patient_details,'doctors':doctor_details,'appointments':appointment_details,'role':'admin'})

    return render(request,'secureHealth/doctorlogin.html')

def registrationpage(request):
    form = registerForm()
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_Password = form.cleaned_data['confirm_Password']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            pincode = form.cleaned_data['pincode']
            mobile_number = form.cleaned_data['mobile_number']
            status = form.cleaned_data['status']

            pRD = patientRegistrationDatas()

            pRD.first_name = enc_decr.encrypt(first_name)
            pRD.last_name = enc_decr.encrypt(last_name)
            pRD.username = enc_decr.encrypt(username)
            pRD.email = enc_decr.encrypt(email)
            pRD.password= enc_decr.encrypt(password)
            pRD.confirm_Password = enc_decr.encrypt(confirm_Password)
            pRD.date_of_birth = date_of_birth
            pRD.address = enc_decr.encrypt(address)
            pRD.blood_group = enc_decr.encrypt(blood_group)
            pRD.gender = enc_decr.encrypt(gender)
            pRD.country = enc_decr.encrypt(country)
            pRD.city = enc_decr.encrypt(city)
            pRD.state = enc_decr.encrypt(state)
            pRD.district = enc_decr.encrypt(district)
            pRD.pincode = enc_decr.encrypt(pincode)
            pRD.mobile_number = enc_decr.encrypt(mobile_number)
            pRD.status= enc_decr.encrypt(status)

            pRD.save()
            return HttpResponse("Registration form is submitted successfully")
        # else:
        # 	return HttpResponse(form.errors)
    return render(request,'secureHealth/registration.html',{'form':form,'role':'admin'})


def patientRecordpage(request):
    form = patientRecordForm()
    if request.method == "POST":
        form = patientRecordForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            blood_group = form.cleaned_data['blood_group']
            age = form.cleaned_data['age']
            phone_number = form.cleaned_data['phone_number']
            haemoglobin = form.cleaned_data['haemoglobin']
            wbc = form.cleaned_data['wbc']
            granulocyte = form.cleaned_data['granulocyte']
            neutrophils = form.cleaned_data['neutrophils']
            platelet_Count = form.cleaned_data['platelet_Count']
            cholestrol = form.cleaned_data['cholestrol']
            triglycerides = form.cleaned_data['triglycerides']
            tsh = form.cleaned_data['tsh']
            bilirubin_total = form.cleaned_data['bilirubin_total']
            globulins = form.cleaned_data['globulins']
            blood_urea = form.cleaned_data['blood_urea']
            albumin = form.cleaned_data['albumin']
            potassium = form.cleaned_data['potassium']
            sodium = form.cleaned_data['sodium']
            message = form.cleaned_data['message']

            pR = patientRecord()
            
            pR.name = enc_decr.encrypt(name)
            pR.blood_group = enc_decr.encrypt(blood_group)
            pR.age = enc_decr.encrypt(age)
            pR.phone_number=enc_decr.encrypt(phone_number)
            pR.haemoglobin = enc_decr.encrypt(haemoglobin)
            pR.wbc =enc_decr.encrypt(wbc)
            pR.granulocyte = enc_decr.encrypt(granulocyte)
            pR.neutrophils = enc_decr.encrypt(neutrophils)
            pR.platelet_Count = enc_decr.encrypt(platelet_Count)
            pR.cholestrol = enc_decr.encrypt(cholestrol)
            pR.triglycerides = enc_decr.encrypt(triglycerides)
            pR.tsh = enc_decr.encrypt(tsh)
            pR.bilirubin_total = enc_decr.encrypt(bilirubin_total)
            pR.globulins= enc_decr.encrypt(globulins)
            pR.blood_urea = enc_decr.encrypt(blood_urea)
            pR.albumin = enc_decr.encrypt(albumin)
            pR.potassium = enc_decr.encrypt(potassium)
            pR.sodium = enc_decr.encrypt(sodium)
            pR.message = enc_decr.encrypt(message)
            pR.save()
            return HttpResponse("Patient records are submitted")
        # else:
        # 	return HttpResponse(form.errors)
    return render(request,'secureHealth/add-patient-record.html',{'form':form})

def patientRecordData(request):
    patient_data = patientRecord.objects.all()
    patients = []
    for p in patient_data:
        name =  enc_decr.decrypt(p.name)
        blood_group =  enc_decr.decrypt(p.blood_group)
        age =  enc_decr.decrypt(p.age)
        phone_number= enc_decr.decrypt(p.phone_number)
        haemoglobin =  enc_decr.decrypt(p.haemoglobin)
        wbc = enc_decr.decrypt(p.wbc)
        granulocyte =  enc_decr.decrypt(p.granulocyte)
        neutrophils =  enc_decr.decrypt(p.neutrophils)
        platelet_Count =  enc_decr.decrypt(p.platelet_Count)
        cholestrol =  enc_decr.decrypt(p.cholestrol)
        triglycerides =  enc_decr.decrypt(p.triglycerides)
        tsh =  enc_decr.decrypt(p.tsh)
        bilirubin_total =  enc_decr.decrypt(p.bilirubin_total)
        globulins=  enc_decr.decrypt(p.globulins)
        blood_urea =  enc_decr.decrypt(p.blood_urea)
        albumin =  enc_decr.decrypt(p.albumin)
        potassium =  enc_decr.decrypt(p.potassium)
        sodium =  enc_decr.decrypt(p.sodium)
        message =  enc_decr.decrypt(p.message)
        decrypt_data = {'id':p.id,'name':name,'age':age,'blood_group':blood_group,'phone_number':phone_number,'haemoglobin':haemoglobin,'wbc':wbc,'granulocyte':granulocyte,'neutrophils':neutrophils,'platelet_Count':platelet_Count,'cholestrol':cholestrol,'triglycerides':triglycerides,'tsh':tsh,'bilirubin_total':bilirubin_total,'globulins':globulins,'blood_urea':blood_urea,'albumin':albumin,'potassium':potassium,'sodium':sodium,'message':message}
        # insert/append decrypt_data(dictionary) into patients(list/tuple)
        patients.append(decrypt_data)
    return render(request,'secureHealth/patient-record.html',{'patient_data':patients,'role':'admin'})


def patientRecordinfo(request):
    patient_data = patientRecord.objects.all()
    name =  enc_decr.decrypt(patient_data.name)
    blood_group =  enc_decr.decrypt(patient_data.blood_group)
    age =  enc_decr.decrypt(patient_data.age)
    phone_number= enc_decr.decrypt(patient_data.phone_number)
    haemoglobin =  enc_decr.decrypt(patient_data.haemoglobin)
    wbc = enc_decr.decrypt(patient_data.wbc)
    granulocyte =  enc_decr.decrypt(patient_data.granulocyte)
    neutrophils =  enc_decr.decrypt(patient_data.neutrophils)
    platelet_Count =  enc_decr.decrypt(patient_data.platelet_Count)
    cholestrol =  enc_decr.decrypt(patient_data.cholestrol)
    triglycerides =  enc_decr.decrypt(patient_data.triglycerides)
    tsh =  enc_decr.decrypt(patient_data.tsh)
    bilirubin_total =  enc_decr.decrypt(patient_data.bilirubin_total)
    globulins=  enc_decr.decrypt(patient_data.globulins)
    blood_urea =  enc_decr.decrypt(patient_data.blood_urea)
    albumin =  enc_decr.decrypt(patient_data.albumin)
    potassium =  enc_decr.decrypt(patient_data.potassium)
    sodium =  enc_decr.decrypt(patient_data.sodium)
    message =  enc_decr.decrypt(patient_data.message)
    decrypt_data = [name,age,blood_group,phone_number,haemoglobin,wbc,granulocyte,neutrophils,platelet_Count,cholestrol,triglycerides,tsh,bilirubin_total,globulins,blood_urea,albumin,potassium,sodium,message]
    return render(request,'secureHealth/patient-record-1.html',{'patient_data':patient_data,'role':'doctor','role':'admin','decrypt_data':decrypt_data})


def editpatientRecord(request,id):
    patient = patientRecord.objects.get(id = id)
    name =  enc_decr.decrypt(patient.name)
    blood_group =  enc_decr.decrypt(patient.blood_group)
    age =  enc_decr.decrypt(patient.age)
    phone_number= enc_decr.decrypt(patient.phone_number)
    haemoglobin =  enc_decr.decrypt(patient.haemoglobin)
    wbc = enc_decr.decrypt(patient.wbc)
    granulocyte =  enc_decr.decrypt(patient.granulocyte)
    neutrophils =  enc_decr.decrypt(patient.neutrophils)
    platelet_Count =  enc_decr.decrypt(patient.platelet_Count)
    cholestrol =  enc_decr.decrypt(patient.cholestrol)
    triglycerides =  enc_decr.decrypt(patient.triglycerides)
    tsh =  enc_decr.decrypt(patient.tsh)
    bilirubin_total =  enc_decr.decrypt(patient.bilirubin_total)
    globulins=  enc_decr.decrypt(patient.globulins)
    blood_urea =  enc_decr.decrypt(patient.blood_urea)
    albumin =  enc_decr.decrypt(patient.albumin)
    potassium =  enc_decr.decrypt(patient.potassium)
    sodium =  enc_decr.decrypt(patient.sodium)
    message =  enc_decr.decrypt(patient.message)
    decrypt_data = [name,age,blood_group,phone_number,haemoglobin,wbc,granulocyte,neutrophils,platelet_Count,cholestrol,triglycerides,tsh,bilirubin_total,globulins,blood_urea,albumin,potassium,sodium,message]
    if request.method == "POST":
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        haemoglobin = request.POST['haemoglobin']
        wbc = request.POST['wbc']
        granulocyte = request.POST['granulocyte']
        neutrophils = request.POST['neutrophils']
        platelet_Count = request.POST['platelet_Count']
        cholestrol = request.POST['cholestrol']
        triglycerides = request.POST['triglycerides']
        tsh = request.POST['tsh']
        bilirubin_total = request.POST['bilirubin_total']
        globulins = request.POST['globulins']
        blood_urea = request.POST['blood_urea']
        albumin = request.POST['albumin']
        potassium = request.POST['potassium']
        sodium = request.POST['sodium']
        message = request.POST['message']

        patient = patientRecord.objects.get(id = id)

        patient.name =  enc_decr.encrypt(name)
        patient.blood_group =  enc_decr.encrypt(blood_group)
        patient.age =  enc_decr.encrypt(age)
        patient.phone_number= enc_decr.encrypt(phone_number)
        patient.haemoglobin =  enc_decr.encrypt(haemoglobin)
        patient.wbc = enc_decr.encrypt(wbc)
        patient.granulocyte =  enc_decr.encrypt(granulocyte)
        patient.neutrophils =  enc_decr.encrypt(neutrophils)
        patient.platelet_Count =  enc_decr.encrypt(platelet_Count)
        patient.cholestrol =  enc_decr.encrypt(cholestrol)
        patient.triglycerides =  enc_decr.encrypt(triglycerides)
        patient.tsh =  enc_decr.encrypt(tsh)
        patient.bilirubin_total =  enc_decr.encrypt(bilirubin_total)
        patient.globulins=  enc_decr.encrypt(globulins)
        patient.blood_urea =  enc_decr.encrypt(blood_urea)
        patient.albumin =  enc_decr.encrypt(albumin)
        patient.potassium =  enc_decr.encrypt(potassium)
        patient.sodium =  enc_decr.encrypt(sodium)
        patient.message =  enc_decr.encrypt(message)
        patient.save()
        return HttpResponse("Patient record updated successfully")

    return render(request,'secureHealth/edit-patient-record.html',{'patient':patient,'role':'admin','decrypt_data':decrypt_data})

def deletepatientRecord(request,id):
    patient = patientRecord.objects.get(id = id)
    patient.delete()
    patient_data = patientRecord.objects.all()
    return render(request,'secureHealth/patient-record.html',{'patient_data':patient_data,'role':'admin'})



def editpatientRecordInfo(request,id):
    patient = patientRecord.objects.get(id = id)
   
    if request.method == "POST":
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        haemoglobin = request.POST['haemoglobin']
        wbc = request.POST['wbc']
        granulocyte = request.POST['granulocyte']
        neutrophils = request.POST['neutrophils']
        platelet_Count = request.POST['platelet_Count']
        cholestrol = request.POST['cholestrol']
        triglycerides = request.POST['triglycerides']
        tsh = request.POST['tsh']
        bilirubin_total = request.POST['bilirubin_total']
        globulins = request.POST['globulins']
        blood_urea = request.POST['blood_urea']
        albumin = request.POST['albumin']
        potassium = request.POST['potassium']
        sodium = request.POST['sodium']
        message = request.POST['message']
       
        patient.name =  enc_decr.encrypt(name)
        patient.blood_group =  enc_decr.encrypt(blood_group)
        patient.age =  enc_decr.encrypt(age)
        patient.phone_number=  enc_decr.encrypt(phone_number)
        patient.haemoglobin = enc_decr.encrypt(haemoglobin)
        patient.wbc =  enc_decr.encrypt(wbc)
        patient.granulocyte =  enc_decr.encrypt(granulocyte)
        patient.neutrophils =  enc_decr.encrypt(neutrophils)
        patient.platelet_Count =  enc_decr.encrypt(platelet_Count)
        patient.cholestrol =  enc_decr.encrypt(cholestrol)
        patient.triglycerides =  enc_decr.encrypt(triglycerides)
        patient.tsh =  enc_decr.encrypt(tsh)
        patient.bilirubin_total =  enc_decr.encrypt(bilirubin_total)
        patient.globulins=  enc_decr.encrypt(globulins)
        patient.blood_urea =  enc_decr.encrypt(blood_urea)
        patient.albumin =  enc_decr.encrypt(albumin)
        patient.potassium =  enc_decr.encrypt(potassium)
        patient.sodium =  enc_decr.encrypt(sodium)
        patient.message =  enc_decr.encrypt(message)
        patient.save()
        return HttpResponse("Patient record updated successfully")

    return render(request,'secureHealth/edit-patient-record.html',{'patient':patient,'role':'doctor','role':'admin'})






