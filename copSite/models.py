from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CopPolicy(models.Model):
    i_accept = models.BooleanField("I ACCEPT the Terms and Condition of the Church of Pentecos", default=True)

TITLE_CHOICES = [('MR', 'Mr'), ('MRS', 'Mrs'), ('SIS', 'Sis'), ('BRO', 'Bro'), ('DEC', 'Dec'), ('DNS', 'Dns'), ('ELD', 'Eld')]
class CopMembership(models.Model):
    suffix = models.CharField(max_length=4, choices=TITLE_CHOICES, null=True)
    f_name = models.CharField(max_length=65)
    m_name = models.CharField(max_length=65)
    l_name = models.CharField(max_length=65)
    birth_date = models.DateField(blank=True, null=True)
    city_of_birth = models.CharField(max_length=100)# This will be city or town of birth
    district_of_birth = models.IntegerField()
    county_of_orgin = models.CharField(max_length=65)
    nationality = models.CharField(max_length=65)
    current_address = models.CharField(max_length=65)
    phone_num = PhoneNumberField(blank=True, null=True)
    email = models.EmailField() # This will be options
    occupation = models.CharField(max_length=65)
    history_of_salvation = models.CharField(max_length=150)# Have you accepted Jesus Charist as your Lord and Savior: YES() NO() if yes, kingly explain how, where and when.
    if_yes = models.CharField(max_length=150)

    #Baptism History
    church = models.CharField(max_length=65)
    location = models.CharField(max_length=65)
    who_conducted_the_baptism = models.CharField(max_length=65)
    type_of_baptism = models.CharField(max_length=65)#sprinking() Immersion() 
    date_of_baptism = models.DateField(blank=True, null=True)
    
    #Parental History
    father_name = models.CharField(max_length=65)
    f_occupation = models.CharField(max_length=65)
    f_religious_affiliation = models.CharField(max_length=65)
    #This will be a radios button
    #Alive() Deceased()
    mother_name = models.CharField(max_length=65)
    m_occupation = models.CharField(max_length=65)
    m_religious_affiliation = models.CharField(max_length=65)
    #This will be a radios button
    #Alive() Deceased()

    #Parental Employment Status
    #employed: YES() NO()
    employment_type = models.CharField(max_length=65)

    # Member Educational background
    institution = models.CharField(max_length=100)
    s_location = models.CharField(max_length=65)
    graduation_year = models.DateField(blank=True, null=True)
    achivement = models.CharField(max_length=65)

    # STATEMENT OF AFFIRAMATION
    """
    I, the undersigned do gereby agree that all information contained herein is to the best of my knowledge,
    true and complete. I do also accept all doctrines and believes of the Church of Pentecost.
    """
    signed = models.CharField(max_length=56)
    cop_policy = models.ManyToManyField(CopPolicy, blank=True)

    # FOR OFFICAL USE ONLY
    this_certifies_that = models.CharField(max_length=65) # This field continue with this text "has met all the requirements to be a member of the Chruch of Pentecost, Praise Temple(Chocolate City Assembly)."
    offical_signed = models.CharField(max_length=65)
    date = models.DateTimeField(auto_now_add=True) # This will be signed by assembly secreatary.
    approved = models.CharField(max_length=65)
    date_approved = models.DateTimeField(auto_now_add=True) # This will be signed by the presiding Elder.