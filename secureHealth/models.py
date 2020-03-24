from django.db import models
 

# Create your models here.


class doctorData(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email =  models.CharField(max_length = 30)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    phone_number =  models.IntegerField()
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    pincode = models.IntegerField()
    mobile_number = models.IntegerField()
    photo = models.FileField(upload_to="images/")
    status = models.CharField(max_length=20)
    short_biography = models.TextField()
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Doctor_Details"
    def __str__(self):

        return self.username


class patientRegistrationDatas(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    email =  models.TextField()
    blood_group= models.TextField()
    password = models.TextField()
    date_of_birth = models.TextField()
    address = models.TextField()
    gender = models.TextField()
    country = models.TextField()
    city = models.TextField(default="tvm")
    state = models.TextField()
    district = models.TextField()
    pincode = models.TextField()
    mobile_number = models.TextField()
    status = models.TextField()
    doctor_name = models.TextField(default="Dr Anitha Samuel")
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Patient Registration Details"
    def __str__(self):

        return self.username


class patientRecord(models.Model):
    name = models.TextField()
    blood_group= models.TextField()
    age =  models.TextField()
    phone_number =  models.TextField()
    haemoglobin = models.TextField()
    wbc = models.TextField()
    granulocyte = models.TextField()
    neutrophils = models.TextField()
    platelet_Count = models.TextField()
    cholestrol = models.TextField()
    triglycerides = models.TextField()
    tsh = models.TextField()
    bilirubin_total = models.TextField()
    globulins = models.TextField()
    blood_urea = models.TextField()
    albumin = models.TextField()
    potassium = models.TextField()
    sodium = models.TextField()
    message = models.TextField()
    doctor_name =models.TextField(default="Dr Anitha Samuel")
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Patient Records"
    def __str__(self):

        return self.name
class adminRegistrations(models.Model):
    
    username = models.CharField(max_length=20)
    email =  models.CharField(max_length = 30)
    mobile_number =  models.IntegerField()
    password = models.CharField(max_length=20)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Admin Registration Details"
    def __str__(self):

        return self.username

class departmentData(models.Model):
    department_name = models.CharField(max_length=60)
    message = models.TextField()
    status = models.CharField(max_length=20)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Departments Available"
    def __str__(self):

        return self.department_name

class settingspage(models.Model):
    hospital_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=20)
    address = models.TextField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    email = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    mobile_number = models.IntegerField()
    fax = models.CharField(max_length=20)
    website_url = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural="Hospital Settings"
    def __str__(self):

        return self.hospital_name

class appointmentspage(models.Model):
    patient_name = models.CharField(max_length=20)
    appointment_id = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    patient_phone_number = models.IntegerField()
    patient_email =  models.CharField(max_length = 100)
    message = models.TextField()
    appointment_status = models.CharField(max_length=20)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Appointment Details"
    def __str__(self):

        return self.appointment_id

class doctorSchedule(models.Model):
    doctor_name = models.CharField(max_length=20)
    available_days = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    message = models.TextField()
    schedule_status = models.CharField(max_length=20)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Doctors Schedule Details"
    def __str__(self):

        return self.doctor_name


class employeeAdd(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email =  models.CharField(max_length = 30)
    password = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20)
    joining_date = models.DateField()
    phone_number = models.IntegerField()
    role = models.TextField()
    status = models.CharField(max_length=20)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Employees Details"
    def __str__(self):

        return self.username

class leaveData(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_role = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=20)
    leave_from = models.DateField()
    leave_to = models.DateField()
    number_of_days =  models.IntegerField()
    remaining_leaves = models.IntegerField()
    leave_reason = models.TextField()
    status = models.CharField(max_length=20)
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Leave Record"
    def __str__(self):

        return self.leave_type

class holidayData(models.Model):
    holiday_name = models.CharField(max_length=20)
    holiday_day = models.CharField(max_length=20)
    holiday_date = models.DateField()
    hospital_name = models.TextField(default="cm hospital")
    class Meta:
        verbose_name_plural="Holidays"
    def __str__(self):

        return self.holiday_name

