from django.db import models
from django.db import connection
from django.forms import ModelForm
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver
import datetime
from django.utils import timezone


# Create your models here.

class Account(models.Model):

	User_id = models.AutoField(primary_key = True)
	Username = models.CharField(max_length = 255, unique = True)
	Password = models.CharField(max_length = 255)
	Verify_Password = models.CharField(max_length = 255)
	Fname = models.CharField(max_length = 255)
	Lname = models.CharField(max_length = 255)
	Email = models.EmailField(max_length = 255)
	Address = models.CharField(max_length = 255)
	# Gender = models.CharField(max_length = 255)
	Contactno = models.CharField(max_length = 255)
	Profile_Pic = models.ImageField(blank=True, upload_to ='display_pictures')

	def __str__(self):

		return self.Username

class ParkingLot(models.Model):

	
	Availability = models.BooleanField(default = False)
	Slot_no = models.IntegerField()

	def __str__(self):
		self.sno = str(self.Slot_no)
		return self.sno


class ReserveParking(models.Model):

	User_id = models.ForeignKey('Account')
	Time_in = models.TimeField()
	Date_in = models.DateField()
	Slot_no = models.IntegerField()
	Plate_no = models.CharField(unique = True, max_length=8)
	Type_of_Vehicle = models.CharField(max_length = 255)
	DateTimeReservation = models.DateTimeField(default = datetime.datetime.now())

	Paid = models.BooleanField(default = False)



	def __str__(self):

		return self.User_id.Username

class CheckoutTicket(models.Model):

	Receipt_no = models.AutoField(primary_key = True)
	Date_in = models.CharField(max_length = 255)
	Time_in = models.CharField(max_length = 255)
	User_id = models.ForeignKey('Account')
	DateTime_out = models.DateTimeField(default = datetime.datetime.now())
	Slotno = models.IntegerField()
	Plateno = models.CharField(max_length = 8)
	Amount_to_be_paid = models.IntegerField()


	def __str__(self):

		self.rno = str(self.Receipt_no)
		return self.rno


class ReservationFee(models.Model):

	Receipt_id = models.AutoField(primary_key = True)
	User_id = models.ForeignKey('Account')
	Customer_Fname = models.CharField(max_length = 255)
	Customer_Lname = models.CharField(max_length = 255)
	Item_Cost = models.PositiveIntegerField()
	Item_Name = models.CharField(max_length = 255)
	Status = models.CharField(max_length = 255)
	DateTime_paid = models.DateTimeField(default = datetime.datetime.now())


	def __str__(self):
		
		self.recno = str(self.Receipt_id)
		return self.recno

class TransactionHistory(models.Model):

	Transact_id = models.AutoField(primary_key = True)
	User_id = models.ForeignKey('Account')
	Receipt_id = models.ForeignKey('ReservationFee')
	Time_in = models.TimeField()
	Date_in = models.DateField()
	DateTime_out = models.DateTimeField()
	Total_Cost = models.PositiveIntegerField()
	Slot_no = models.IntegerField()
	Plate_no = models.CharField(max_length = 8)
	Fname = models.CharField(max_length = 255)
	Lname = models.CharField(max_length = 255)
	

	def __str__(self):
		return self.Plate_no



# def show_me_the_money(sender, **kwargs):
#    """signal function"""
#    ipn_obj = sender
#    if ipn_obj.payment_status == ST_PP_COMPLETED:

#    		if ipn_obj.receiver_email != "parking.payments1@gmail.com":


#    			if ipn_obj.mc_gross == price and ipn.mc_currency == 'USD':
#       			 print('working')
#    		else:
#       		 print("not working")



# valid_ipn_received.connect(show_me_the_money)



# print("handlers.py has been imported")