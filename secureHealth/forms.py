from django import forms

class registerForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget =forms.PasswordInput)
    confirm_Password = forms.CharField(widget = forms.PasswordInput)
    date_of_birth = forms.DateField()
    address = forms.CharField()
    choice= [
        ('O+ve', 'O+ve'),
        ('O-ve','O-ve'),
        ('A+ve', 'A+ve'),
        ('A-ve', 'A-ve'),
        ('B+ve', 'B+ve'),
        ('B-ve', 'B-ve'),
        ('AB+ve', 'AB+ve'),
        ('AB-ve', 'AB-ve'),
    ]
    blood_group = forms.CharField(label='Blood Group', widget=forms.Select(choices=choice))
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    country = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    district = forms.CharField()
    pincode = forms.CharField(widget=forms.NumberInput)
    mobile_number = forms.CharField(widget=forms.NumberInput)
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    status =forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())
    DOCTOR_CHOICES = (
        ('dranitha12', 'Dr Anitha Samuel'),
        ('drramesh23', 'Dr Ramesh Raj'),
        ('drveena78', 'Dr Veena Madhavan'),
        ('drrashmika235', 'Dr Rashmika Yash'),
        ('drshanthi09', 'Dr shanthi Sarogam'),
        ('drmathew89', 'Dr Mathew Vargheese'),
    )
    doctor = forms.CharField(label='Department', widget=forms.Select(choices=DOCTOR_CHOICES))
    
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    def clean_username(self):
        value = self.cleaned_data['username']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value
    
    def clean_confirm_Password(self):
       password = self.cleaned_data['password']
       confirm_Password = self.cleaned_data['confirm_Password']
       if not password == confirm_Password:
            raise forms.ValidationError("Password and Confirm Password not match")
       return password



class doctorDataForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget =forms.PasswordInput)
    confirm_Password = forms.CharField(widget = forms.PasswordInput)
    date_of_birth = forms.DateField()
    address = forms.CharField()
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    country = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    phone_number = forms.CharField(widget=forms.NumberInput)
    state = forms.CharField()
    district = forms.CharField()
    pincode = forms.CharField(widget=forms.NumberInput)
    mobile_number = forms.CharField(widget=forms.NumberInput)
    photo=forms.FileField()
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    status =forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())
    short_biography = forms.CharField(widget=forms.Textarea())

    def clean_username(self):
        value = self.cleaned_data['username']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value
    
    def clean_confirm_Password(self):
       password = self.cleaned_data['password']
       confirm_Password = self.cleaned_data['confirm_Password']
       if not password == confirm_Password:
            raise forms.ValidationError("Password and Confirm Password not match")
       return password
    
class patientRecordForm(forms.Form):
    name = forms.CharField()
    choice= [
        ('O+ve', 'O+ve'),
        ('O-ve','O-ve'),
        ('A+ve', 'A+ve'),
        ('A-ve', 'A-ve'),
        ('B+ve', 'B+ve'),
        ('B-ve', 'B-ve'),
        ('AB+ve', 'AB+ve'),
        ('AB-ve', 'AB-ve'),
    ]
    blood_group = forms.CharField(label='Blood Group', widget=forms.Select(choices=choice))
    DOCTOR_CHOICES = (
        ('dranitha12', 'Dr Anitha Samuel'),
        ('drramesh23', 'Dr Ramesh Raj'),
        ('drveena78', 'Dr Veena Madhavan'),
        ('drrashmika235', 'Dr Rashmika Yash'),
        ('drshanthi09', 'Dr shanthi Sarogam'),
        ('drmathew89', 'Dr Mathew Vargheese'),
    )
    doctor_name= forms.CharField(label='Department', widget=forms.Select(choices=DOCTOR_CHOICES))
    
    username = forms.CharField()
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    age = forms.CharField(widget=forms.NumberInput)
    phone_number = forms.CharField(widget=forms.NumberInput)
    haemoglobin = forms.CharField()
    wbc = forms.CharField()
    granulocyte = forms.CharField()
    neutrophils = forms.CharField()
    platelet_Count = forms.CharField()
    cholestrol = forms.CharField()
    triglycerides = forms.CharField()
    tsh = forms.CharField()
    bilirubin_total = forms.CharField()
    globulins = forms.CharField()
    blood_urea = forms.CharField()
    albumin = forms.CharField()
    potassium = forms.CharField()
    sodium = forms.CharField()
    message = forms.CharField()

class adminRegistrationForm(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    mobile_number = forms.CharField(widget=forms.NumberInput)
    password = forms.CharField(widget =forms.PasswordInput)
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    

    def clean_username(self):
        value = self.cleaned_data['username']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value


class departmentForm(forms.Form):
    department_name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    status =forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())
    def clean_department_name(self):
        value = self.cleaned_data['department_name']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value



class settingsForm(forms.Form):
    hospital_name = forms.CharField()
    contact_person = forms.CharField()
    address = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pincode = forms.CharField(widget=forms.NumberInput)
    email = forms.EmailField(widget=forms.EmailInput)
    phone_number = forms.CharField(widget=forms.NumberInput)
    mobile_number = forms.CharField(widget=forms.NumberInput)
    fax = forms.CharField()
    website_url = forms.CharField()
    def clean_contact_person(self):
        value = self.cleaned_data['contact_person']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value

class appointmentForm(forms.Form):
    patient_name = forms.CharField()
    appointment_id = forms.CharField()
    DEPARTMENT_CHOICES = (
            ('Dentists', 'Dentists'),
            ('Neurology', 'Neurology'),
            ('Opthalmology', 'Opthalmology'),
            ('Orthopedics', 'Orthopedics'),
            ('Cancer Department', 'Cancer Department'),
            ('ENT Department', 'ENT Department'),
        )
    department = forms.CharField(label='Department', widget=forms.Select(choices=DEPARTMENT_CHOICES))
    DOCTOR_CHOICES = (
        ('dranitha12', 'Dr Anitha Samuel'),
        ('drramesh23', 'Dr Ramesh Raj'),
        ('drveena78', 'Dr Veena Madhavan'),
        ('drrashmika235', 'Dr Rashmika Yash'),
        ('drshanthi09', 'Dr shanthi Sarogam'),
        ('drmathew89', 'Dr Mathew Vargheese'),
    )
    doctor = forms.CharField(label='Department', widget=forms.Select(choices=DOCTOR_CHOICES))
    date = forms.DateField()
    time = forms.TimeField()
    patient_phone_number = forms.CharField(widget=forms.NumberInput)
    patient_email =  forms.EmailField(widget=forms.EmailInput)
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    message = forms.CharField(widget=forms.Textarea())
    APPOINTMENT_STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    appointment_status = forms.ChoiceField(choices=APPOINTMENT_STATUS_CHOICES, widget=forms.RadioSelect())
    def clean_patient_name(self):
        value = self.cleaned_data['patient_name']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value

class doctorScheduleForm(forms.Form):
    
    available_days = forms.CharField()
    start_time = forms.TimeField()
    DOCTOR_CHOICES = (
        ('dranitha12', 'Dr Anitha Samuel'),
        ('drramesh23', 'Dr Ramesh Raj'),
        ('drveena78', 'Dr Veena Madhavan'),
        ('drrashmika235', 'Dr Rashmika Yash'),
        ('drshnthi09', 'Dr shanthi Sarogam'),
        ('drmathew89', 'Dr Mathew Vargheese'),
    )
    doctor_name = forms.CharField(label='Doctor Name', widget=forms.Select(choices=DOCTOR_CHOICES))
    end_time = forms.TimeField()
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    message = forms.CharField(widget=forms.Textarea())
    SCHEDULE_STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    schedule_status = forms.ChoiceField(choices=SCHEDULE_STATUS_CHOICES, widget=forms.RadioSelect())

class employeeForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget =forms.PasswordInput)
    confirm_Password = forms.CharField(widget = forms.PasswordInput)
    employee_id = forms.CharField()
    joining_date = forms.DateField()
    phone_number = forms.CharField(widget=forms.NumberInput)
    ROLES_CHOICES = (
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Laboratorist', 'Laboratorist'),
        ('Pharmacist', 'Dr shanthi Sarogam'),
        ('Pharmacist', 'Pharmacist'),
        ('Receptionist', 'Receptionist'),
    )
    role = forms.CharField(label='Role', widget=forms.Select(choices=ROLES_CHOICES))
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    status =forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())

    def clean_username(self):
        value = self.cleaned_data['username']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value

    def clean_confirm_Password(self):
       password = self.cleaned_data['password']
       confirm_Password = self.cleaned_data['confirm_Password']
       if not password == confirm_Password:
            raise forms.ValidationError("Password and Confirm Password not match")
       return password

class leaveForm(forms.Form):
    employee_id = forms.CharField()
    ROLES_CHOICES = (
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Laboratorist', 'Laboratorist'),
        ('Pharmacist', 'Dr shanthi Sarogam'),
        ('Pharmacist', 'Pharmacist'),
        ('Receptionist', 'Receptionist'),
    )
    employee_role = forms.CharField(label='Role', widget=forms.Select(choices=ROLES_CHOICES))
    leave_from = forms.DateField()
    LEAVE_TYPE_CHOICES= (
        ('Casual Leave', 'Casual Leave'),
        ('Medical Leave', 'Medical Leave'),
        ('Loss of Pay', 'Loss of Pay'),
    )
    leave_type = forms.CharField(label='Leave Type', widget=forms.Select(choices=LEAVE_TYPE_CHOICES))
    leave_to = forms.DateField()
    number_of_days =  forms.CharField(widget=forms.NumberInput)
    remaining_leaves = forms.CharField(widget=forms.NumberInput)
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    leave_reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 10,'cols': 20}))

class holidayForm(forms.Form):
    holiday_name = forms.CharField()
    HOLIDAY_CHOICES = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    holiday_day = forms.CharField(label='Role', widget=forms.Select(choices=HOLIDAY_CHOICES))
    Hospital_CHOICES = (
        ('cm hospital', 'cm hospital'),
        ('kims hospital', 'kims hospital'),
    )
    hospital_name = forms.CharField(label='Hospital Name', widget=forms.Select(choices=Hospital_CHOICES))
    
    holiday_date = forms.DateField()