from django.shortcuts import render, redirect
from Project.models import Account, ParkingLot, ReserveParking, CheckoutTicket, ReservationFee, TransactionHistory
from django.http import HttpResponse
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import datetime



Paid = False
datenow = datetime.date.today()
timenow = datetime.datetime.now().time()
now = datetime.datetime.now()



@csrf_exempt
def payment_done(request):

	if 'logged_in' and 'reserve_slot' in request.session:

		if request.method == 'POST' and 'success' in request.POST:

			AccLogged = Account.objects.get(Username = request.session['username'])
			ChoicedSlot = ReserveParking.objects.get(User_id_id = AccLogged.User_id)
			ParkingLot.objects.filter(Slot_no = ChoicedSlot.Slot_no).update(Availability = 0)
			ReserveParking.objects.filter(Plate_no = ChoicedSlot.Plate_no).update(Paid = 1)
			SuccPayment = ReservationFee(User_id_id = AccLogged.User_id, Customer_Fname = AccLogged.Fname, Customer_Lname = AccLogged.Lname, Item_Cost = 50, Item_Name = "Reservation_Fee", Status = "Success")
			SuccPayment.save()

			request.session['Paid'] = True
			return redirect('index')

	else:

		return HttpResponse("Invalid Access")

	return render(request, 'Project/success.html')

@csrf_exempt
def payment_cancelled(request):

	if 'logged_in' and 'reserve_slot' in request.session:

		if request.method == 'POST' and 'failed' in request.POST:

			AccLogged = Account.objects.get(Username = request.session['username'])
			FailPayment = ReservationFee(User_id_id = AccLogged.User_id, Customer_Fname = AccLogged.Fname, Customer_Lname = AccLogged.Lname, Item_Cost = 25, Item_Name = "Reservation_Fee", Status = "Cancelled")
			FailPayment.save()
			ReserveParking.objects.filter(Plate_no = ChoicedSlot.Plate_no).delete()
			request.session['Paid'] = False
			return redirect('index')
	else:

		return HttpResponse("Invalid Access")

	return render(request, 'Project/failed.html')


def frontpage(request):

	if 'logged_in' in request.session:

		return redirect('index')

	else:

		return render(request, 'Project/home.html')


def login(request):

	if 'logged_in' in request.session:

		return redirect('index')
	else:

		if request.method == 'POST' and 'login' in request.POST:


			username = request.POST['user']
			password_check = request.POST['pass']



			
			if (Account.objects.filter(Username = username, Password = password_check)):


			

				ac = Account.objects.get(Username = username, Password = password_check)

				
				request.session['logged_in'] = True
				print("Successfully logged in")
				request.session['username'] = username
				return redirect('index')


			else:

				request.session['logged_in'] = False
				request.session.flush()
				print("Incorrect username or password")
				context = {'error' : '1'}
				return render(request, 'Project/login.html', context)


	return render(request, 'Project/login.html')

def register(request):

	if 'logged_in' in request.session:

		print("Already logged_in redirecting to index page")
		return redirect('index')

	else:

		print("Register account")
		context = {

		}

		if request.method == 'POST' and 'register' in request.POST:

			username = request.POST['username']
			password = request.POST['password']
			confirmpassword = request.POST['confirmpassword']
			email = request.POST['email']
			address = request.POST['address']
			contactno = request.POST['contactno']
			fname = request.POST['fname']
			lname = request.POST['lname']

			RegAcc = Account(Username = username, Password = password, Verify_Password = confirmpassword, Fname = fname, Lname = lname, Email = email, Address = address, Contactno = contactno)

			if password == confirmpassword:

				isUsernameExist = Account.objects.filter(Username = username).exists()

				if isUsernameExist == False:


					if fname.isalpha() and lname.isalpha():

						RegAcc.save()
						return redirect('frontpage')

					else:

						context = {'error' : 2, 'success' : 0}
						return render(request, 'Project/register2.html', context)

				else:

					context = {'error' : 1, 'success' : 0} #print Username already used
					return render(request, 'Project/register2.html', context)

			else:

				context = {'error' : 0, 'success' : 0} #print password does not match
				return render(request, 'Project/register2.html', context)



		return render(request, 'Project/register2.html')
		



def index(request):

	print("Here!")
	

	if 'logged_in' in request.session:

		a = Account.objects.get(Username = request.session['username'])
				
		print("Redirecting to index page")

		
		Information = Account.objects.filter(User_id = a.User_id)


		availableslots = ParkingLot.objects.filter(Availability = 1)


		s1 = ParkingLot.objects.get(Slot_no = 1)
		s2 = ParkingLot.objects.get(Slot_no = 2)
		s3 = ParkingLot.objects.get(Slot_no = 3) 
		s4 = ParkingLot.objects.get(Slot_no = 4)
		s5 = ParkingLot.objects.get(Slot_no = 5)
		s6 = ParkingLot.objects.get(Slot_no = 6)
		s7 = ParkingLot.objects.get(Slot_no = 7)
		s8 = ParkingLot.objects.get(Slot_no = 8)
		s9 = ParkingLot.objects.get(Slot_no = 9)
		s10 = ParkingLot.objects.get(Slot_no = 10)
		s11 = ParkingLot.objects.get(Slot_no = 11)
		s12 = ParkingLot.objects.get(Slot_no = 12)
		s13 = ParkingLot.objects.get(Slot_no = 13)
		s14 = ParkingLot.objects.get(Slot_no = 14)
		s15 = ParkingLot.objects.get(Slot_no = 15)
		s16 = ParkingLot.objects.get(Slot_no = 16)
		s17 = ParkingLot.objects.get(Slot_no = 17)
		s18 = ParkingLot.objects.get(Slot_no = 18)
		s19 = ParkingLot.objects.get(Slot_no = 19)
		s20 = ParkingLot.objects.get(Slot_no = 20)
		s21 = ParkingLot.objects.get(Slot_no = 21)
		s22 = ParkingLot.objects.get(Slot_no = 22)
		s23 = ParkingLot.objects.get(Slot_no = 23)
		s24 = ParkingLot.objects.get(Slot_no = 24)
		s25 = ParkingLot.objects.get(Slot_no = 25)
		s26 = ParkingLot.objects.get(Slot_no = 26)
		s27 = ParkingLot.objects.get(Slot_no = 27)
		s28 = ParkingLot.objects.get(Slot_no = 28)
		isAlreadyReserve = ReserveParking.objects.filter(User_id_id = a.User_id, Paid = 1).exists()
		isAlreadyReserveNotPaid = ReserveParking.objects.filter(User_id_id = a.User_id, Paid = 0).exists()
		


		if isAlreadyReserve == True :

			context = {'reserve' : 1, 'username' : a.Username, 'slotno' : availableslots, 'Information' : Information,
			'slot1' : s1.Availability,
			'slot2' : s2.Availability,
			'slot3' : s3.Availability,
			'slot4' : s4.Availability,
			'slot5' : s5.Availability,
			'slot6' : s6.Availability,
			'slot7' : s7.Availability,
			'slot8' : s8.Availability,
			'slot9' : s9.Availability,
			'slot10' : s10.Availability,
			'slot11' : s11.Availability,
			'slot12' : s12.Availability,
			'slot13' : s13.Availability,
			'slot14' : s14.Availability,
			'slot15' : s15.Availability,
			'slot16' : s16.Availability,
			'slot17' : s17.Availability,
			'slot18' : s18.Availability,
			'slot19' : s19.Availability,
			'slot20' : s20.Availability,
			'slot21' : s21.Availability,
			'slot22' : s22.Availability,
			'slot23' : s23.Availability,
			'slot24' : s24.Availability,
			'slot25' : s25.Availability,
			'slot26' : s26.Availability,
			'slot27' : s27.Availability,
			'slot28' : s28.Availability,}
			
			print("Has reservation")

		elif isAlreadyReserveNotPaid == True:



			request.session['reserve_slot'] = True
			context = {'reserve' : 2, 'username' : a.Username, 'slotno' : availableslots, 'Information' : Information,
			'slot1' : s1.Availability,
			'slot2' : s2.Availability,
			'slot3' : s3.Availability,
			'slot4' : s4.Availability,
			'slot5' : s5.Availability,
			'slot6' : s6.Availability,
			'slot7' : s7.Availability,
			'slot8' : s8.Availability,
			'slot9' : s9.Availability,
			'slot10' : s10.Availability,
			'slot11' : s11.Availability,
			'slot12' : s12.Availability,
			'slot13' : s13.Availability,
			'slot14' : s14.Availability,
			'slot15' : s15.Availability,
			'slot16' : s16.Availability,
			'slot17' : s17.Availability,
			'slot18' : s18.Availability,
			'slot19' : s19.Availability,
			'slot20' : s20.Availability,
			'slot21' : s21.Availability,
			'slot22' : s22.Availability,
			'slot23' : s23.Availability,
			'slot24' : s24.Availability,
			'slot25' : s25.Availability,
			'slot26' : s26.Availability,
			'slot27' : s27.Availability,
			'slot28' : s28.Availability,}




		else:

			context = {'reserve' : '0', 'username' : a.Username, 'slotno' : availableslots, 'Information' : Information,
			'slot1' : s1.Availability, 
			'slot2' : s2.Availability,
			'slot3' : s3.Availability,
			'slot4' : s4.Availability,
			'slot5' : s5.Availability,
			'slot6' : s6.Availability,
			'slot7' : s7.Availability,
			'slot8' : s8.Availability,
			'slot9' : s9.Availability,
			'slot10' : s10.Availability,
			'slot11' : s11.Availability,
			'slot12' : s12.Availability,
			'slot13' : s13.Availability,
			'slot14' : s14.Availability,
			'slot15' : s15.Availability,
			'slot16' : s16.Availability,
			'slot17' : s17.Availability,
			'slot18' : s18.Availability,
			'slot19' : s19.Availability,
			'slot20' : s20.Availability,
			'slot21' : s21.Availability,
			'slot22' : s22.Availability,
			'slot23' : s23.Availability,
			'slot24' : s24.Availability,
			'slot25' : s25.Availability,
			'slot26' : s26.Availability,
			'slot27' : s27.Availability,
			'slot28' : s28.Availability,}
			
			

			
			print("Reserving a slot....")

	
		
		if(request.method == 'POST' and 'reserve' in request.POST):

			time = request.POST['timein']
			date = request.POST['datein']
			plateno = request.POST['plateno']
			tov = request.POST['tov']
			slotnumber = request.POST['slot']

			
			ac = ReserveParking(User_id_id = a.User_id, Slot_no = slotnumber, Date_in = date, Time_in = time, Plate_no = plateno, Type_of_Vehicle = tov, Paid = False)

			
			isExist = ReserveParking.objects.filter(Plate_no=plateno).exists() #throws a boolean either true or false
		

			


			if isExist == False:

				if datetime.datetime.strptime(date, "%Y-%m-%d").date() >= datenow:


					if (datetime.datetime.strptime(time, "%H:%M").time() < timenow and datetime.datetime.strptime(date, "%Y-%m-%d").date() > datenow) or (datetime.datetime.strptime(time, "%H:%M").time() > timenow):

						ac.save()
						request.session['reserve_slot'] = True
						request.session['Paid'] = False
						return redirect('payment_process')
						

					else:

						context = {'reserve':'0', 'username':a.Username, 'slotno': availableslots, 'error': 3, 'Information' : Information,
								'slot1' : s1.Availability, 
								'slot2' : s2.Availability,
								'slot3' : s3.Availability,
								'slot4' : s4.Availability,
								'slot5' : s5.Availability,
								'slot6' : s6.Availability,
								'slot7' : s7.Availability,
								'slot8' : s8.Availability,
								'slot9' : s9.Availability,
								'slot10' : s10.Availability,
								'slot11' : s11.Availability,
								'slot12' : s12.Availability,
								'slot13' : s13.Availability,
								'slot14' : s14.Availability,
								'slot15' : s15.Availability,
								'slot16' : s16.Availability,
								'slot17' : s17.Availability,
								'slot18' : s18.Availability,
								'slot19' : s19.Availability,
								'slot20' : s20.Availability,
								'slot21' : s21.Availability,
								'slot22' : s22.Availability,
								'slot23' : s23.Availability,
								'slot24' : s24.Availability,
								'slot25' : s25.Availability,
								'slot26' : s26.Availability,
								'slot27' : s27.Availability,
								'slot28' : s28.Availability,}
						print("The time is not acceptable")
						request.session['reserve_slot'] = False
						return render(request, 'Project/index3.html', context)

				

				else:
					context = {'reserve' : '0', 'username' : a.Username, 'slotno' : availableslots, 'error' : 2, 'Information' : Information,
								'slot1' : s1.Availability,
								'slot2' : s2.Availability,
								'slot3' : s3.Availability,
								'slot4' : s4.Availability,
								'slot5' : s5.Availability,
								'slot6' : s6.Availability,
								'slot7' : s7.Availability,
								'slot8' : s8.Availability,
								'slot9' : s9.Availability,
								'slot10' : s10.Availability,
								'slot11' : s11.Availability,
								'slot12' : s12.Availability,
								'slot13' : s13.Availability,
								'slot14' : s14.Availability,
								'slot15' : s15.Availability,
								'slot16' : s16.Availability,
								'slot17' : s17.Availability,
								'slot18' : s18.Availability,
								'slot19' : s19.Availability,
								'slot20' : s20.Availability,
								'slot21' : s21.Availability,
								'slot22' : s22.Availability,
								'slot23' : s23.Availability,
								'slot24' : s24.Availability,
								'slot25' : s25.Availability,
								'slot26' : s26.Availability,
								'slot27' : s27.Availability,
								'slot28' : s28.Availability,}
					print("The date is not acceptable")
					request.session['reserve_slot'] = False
					return render(request, 'Project/index3.html', context)
			else:
				context = {'reserve' : '0', 'username' : a.Username, 'slotno' : availableslots, 'error' : 1, 'Information' : Information,
							'slot1' : s1.Availability,
							'slot2' : s2.Availability,
							'slot3' : s3.Availability,
							'slot4' : s4.Availability,
							'slot5' : s5.Availability,
							'slot6' : s6.Availability,
							'slot7' : s7.Availability,
							'slot8' : s8.Availability,
							'slot9' : s9.Availability,
							'slot10' : s10.Availability,
							'slot11' : s11.Availability,
							'slot12' : s12.Availability,
							'slot13' : s13.Availability,
							'slot14' : s14.Availability,
							'slot15' : s15.Availability,
							'slot16' : s16.Availability,
							'slot17' : s17.Availability,
							'slot18' : s18.Availability,
							'slot19' : s19.Availability,
							'slot20' : s20.Availability,
							'slot21' : s21.Availability,
							'slot22' : s22.Availability,
							'slot23' : s23.Availability,
							'slot24' : s24.Availability,
							'slot25' : s25.Availability,
							'slot26' : s26.Availability,
							'slot27' : s27.Availability,
							'slot28' : s28.Availability,}
				return render(request, 'Project/index3.html', context)
				request.session['reserve_slot'] = False
				print("Duplicate plate number is not allowed")
				

		if(request.method == 'POST' and 'logged_out' in request.POST):

			request.session['logged_in'] = False
			request.session.flush()
			print("Logged_out")
			return redirect('frontpage')

		if(request.method == 'POST' and 'editprofile' in request.POST):

			return redirect('editprofile')


	else:

		return HttpResponse("Invalid access")


	return render(request, 'Project/index3.html', context)

	


def checkout(request):

	AccLogged = Account.objects.get(Username = request.session['username'])
	print(AccLogged.User_id)
	ChoicedSlot = ReserveParking.objects.get(User_id_id = AccLogged.User_id)
	SuccReserveFee = ReservationFee.objects.get(User_id_id = AccLogged.User_id, Receipt_id = 4)

	if 'logged_in' in request.session and ChoicedSlot.Paid == 1:

		

		DispOut = ReserveParking.objects.filter(User_id_id = AccLogged.User_id)
		context = {'Information' : DispOut}

		if(request.method == 'POST' and 'checkout' in request.POST):

			
			ParkingLot.objects.filter(Slot_no = ChoicedSlot.Slot_no).update(Availability = 1)
			request.session['checkout'] = True

			delta = datetime.timedelta(hours = 2)
			timeforpayment = ChoicedSlot.DateTimeReservation + delta

			if(timeforpayment >= ChoicedSlot.DateTimeReservation):
				amount = 50 + 50
				

				Ticket = CheckoutTicket(User_id_id = AccLogged.User_id, Amount_to_be_paid = amount, Plateno = ChoicedSlot.Plate_no, Slotno = ChoicedSlot.Slot_no, Time_in = ChoicedSlot.Time_in, Date_in = ChoicedSlot.Date_in)
				Ticket.save()

				print("Ticket has been saved")

				TicketInfo = CheckoutTicket.objects.get(User_id_id = AccLogged.User_id, Plateno = ChoicedSlot.Plate_no, Slotno = ChoicedSlot.Slot_no, Date_in = ChoicedSlot.Date_in, Time_in = ChoicedSlot.Time_in)
				print(AccLogged.User_id, SuccReserveFee.Receipt_id, ChoicedSlot.id,  ChoicedSlot.Time_in,  ChoicedSlot.Date_in, TicketInfo.DateTime_out, TicketInfo.Amount_to_be_paid, ChoicedSlot.Slot_no)
				Transact = TransactionHistory(Fname = AccLogged.Fname, Lname = AccLogged.Lname, User_id_id = AccLogged.User_id, Receipt_id_id = SuccReserveFee.Receipt_id, Time_in = TicketInfo.Time_in, Date_in = TicketInfo.Date_in, DateTime_out = TicketInfo.DateTime_out, Total_Cost = TicketInfo.Amount_to_be_paid, Slot_no = TicketInfo.Slotno, Plate_no = TicketInfo.Plateno)
				print(Transact)
				Transact.save() 

				print("Transaction has been saved")

				ReserveParking.objects.filter(User_id_id = AccLogged.User_id).delete()

				return redirect('index') 


	else:

		return HttpResponse("INVALID ACCESS")

	return render(request, 'Project/checkout.html', context)


def update(request):


	AccLogged = Account.objects.get(Username = request.session['username'])

	if 'logged_in' in request.session :

		
		CstmrSlotNo = ReserveParking.objects.get(User_id_id = AccLogged.User_id)

		if request.method == 'POST' and 'update' in request.POST:

			time = request.POST['timein']
			date = request.POST['datein']
			plateno = request.POST['plateno']
			tov = request.POST['tov']
			slotnumber = request.POST['slot']

			



			if datetime.datetime.strptime(date, "%Y-%m-%d").date() >= datenow:

				if (datetime.datetime.strptime(time, "%H:%M").time() < timenow and datetime.datetime.strptime(date, "%Y-%m-%d").date() > datenow) or (datetime.datetime.strptime(time, "%H:%M").time() > timenow):


					PrevSlot_no = ReserveParking.objects.get(User_id_id = AccLogged.User_id)
					ParkingLot.objects.filter(Slot_no = PrevSlot_no.Slot_no).update(Availability = 1)
					ReserveParking.objects.filter(User_id_id = AccLogged.User_id).update(User_id_id = AccLogged.User_id, Slot_no = slotnumber, Date_in = date, Time_in = time, Plate_no = plateno, Type_of_Vehicle = tov)
					ParkingLot.objects.filter(Slot_no = slotnumber).update(Availability = 0)
					return redirect('checkout')


				else:

					context = {'SlotNumber' : CstmrSlotNo, 'error': 3}
					print("The time is not acceptable")
					return render(request, 'Project/update2.html', context)
			else:
				context = {'SlotNumber' : CstmrSlotNo, 'error' : 2}
				print("The date is not acceptable")					
				return render(request, 'Project/update2.html', context)
	else:
		return HttpResponse("Invalid Access")

	context = {'SlotNumber' : CstmrSlotNo}
	return render(request, 'Project/update2.html', context)


def payment_process(request):

	if 'logged_in' in request.session:

		order_id = request.session.get('User_id_id')

		if request.method == 'POST' and 'cancelled' in request.POST:

			AccLogged = Account.objects.get(Username = request.session['username'])
			print(AccLogged.User_id)
			ReserveParking.objects.filter(User_id_id = AccLogged.User_id).delete()
			return redirect('index')

		else:

			paypal_dict = {

			"business" : settings.PAYPAL_RECEIVER_EMAIL,
			"amount" : "50",
			"item_name" : "Reservation Fee",
			"invoice" : str(order_id), #This will be serve as invoice number the User_id_id.
			'currency_code' : 'PHP',
			"notify_url" : request.build_absolute_uri(reverse('paypal-ipn')),
			"return_url" : request.build_absolute_uri(reverse('payment_done')),
			"cancel_return" : request.build_absolute_uri(reverse('payment_cancelled')),


			}		
			form = PayPalPaymentsForm(initial=paypal_dict)
			context = { "form" : form }
			

		
	else:
		return HttpResponse("Invalid Access")

	return render(request, "Project/paypal.html", context)


def CancelReservation(request):

	if 'logged_in' in request.session:

		AccLogged = Account.objects.get(Username = request.session['username'])


		if request.method == 'POST' and 'cancelled' in request.POST:

			ReserveParking.objects.filter(User_id_id = AccLogged.User_id).delete()
			return redirect('index')

	return render(request, 'Project/cancel.html')

def editprofile(request):

	if 'logged_in' in request.session:

		AccLogged = Account.objects.get(Username = request.session['username'])
		AccInfo = Account.objects.filter(User_id = AccLogged.User_id)

		if request.method == 'POST' and  'updateprofile' in request.POST:

			fname = request.POST['fname']
			lname = request.POST['lname']
			oldpass = request.POST['oldpass']
			newpass = request.POST['newpass']
			confirmpass = request.POST['confirmpass']
			email = request.POST['email']
			contactno = request.POST['contactno']
			address = request.POST['address']




			if oldpass == AccLogged.Password:

				if newpass == confirmpass:


					Account.objects.filter(User_id = AccLogged.User_id).update(Password = newpass, Verify_Password = confirmpass, Fname = fname, Lname = lname, Email = email, Address = address, Contactno = contactno)
					print('profile_updated')

					if 'profile_pic' in request.FILES:
						print('gotcha')
						Account.objects.filter(User_id = AccLogged.User_id).update(Profile_Pic = request.FILES['profile_pic'])
						url = Account.objects.get(User_id = AccLogged.User_id)
						print(url.Profile_Pic.path)
						# profile_pic = request.FILES['profile_pic']
						# fs = FileSystemStorage()
						# filename = fs.save(profile_pic.name, profile_pic)
						# uploaded_file_url = fs.url(filename)
							
				
					print("Profile Updated!")
					return render(request, 'Project/profile.html', { 'AccInfo':AccInfo})

				else:
			
					return render(request, 'Project/profile.html', {'error':2, 'AccInfo' : AccInfo})

			else:
				
				return render(request, 'Project/profile.html', {'error': 1, 'AccInfo' : AccInfo})
			
	context = {'AccInfo' : AccInfo}
	return render(request, 'Project/profile.html', context)

def termsofservice(request):

	return render(request, 'Project/tos.html')

def privacy(request):

	return render(request, 'Project/privacy.html')








