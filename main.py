# from django.contrib.auth.models import AbstractUser
#
#
# class Profile
#     ROLE_CHOICES = [
#         ('admin','admin'),
#         ('doctor','doctor'),
#         ('nurse', 'nurse'),
#         ('receptionist','receptionist'),
#         ('patient','patient'),
#     ]
#
#     role
#     phone_number
#
#
# class Patient
#     user
#     date_of_birth
#     address
#
#
# class Doctor
#     specialty
#     qualifications
#     experience_year
#
#
#
# class Nurse(models.Model):
#     department
#
#
# class Department
#     name =
#     head
#
# class Appointment
#
#     STATUS_CHOICES
#     patient
#     doctor
#     date_time
#     status
#     notes
#
# class MedicalRecord
#
#
#     patient
#     doctor
#     diagnosis
#     treatment
#     created_at
#
#
# class Prescription
#
#     patient
#     doctor
#     medication
#     dosage
#     created_at
#
#
# class Billing
#
#     patient
#     total_amount
#     paid
#     issued_date
#
#
#
# class Ward
#
#     name
#     capacity
#
# class Admission(models.Model):
#
#     patient
#     ward
#     admitted_on
#     discharged_on
#
#
#
# class Feedback(models.Model):
#
#     doctor
#     patient
#     content
#     created_at
