from django.conf.urls import url
from Project import views

urlpatterns = [

		url(r'^$', views.frontpage, name = 'frontpage'),
		url(r'^home/$', views.index, name = 'index'),
		url(r'^login/$', views.login, name = 'login'),
		url(r'^register/$', views.register, name = 'register'),
		url(r'^home/checkout/$', views.checkout, name = 'checkout'),
		url(r'^home/updateReservation/$', views.update, name = 'update'),
		url(r'^home/done/$', views.payment_done, name = 'payment_done'),
		url(r'^home/cancelled/$', views.payment_cancelled, name = 'payment_cancelled'),
		url(r'^home/process/$', views.payment_process, name = 'payment_process'),
		url(r'^home/cancelreservation/$', views.CancelReservation, name = 'CancelReservation'),
		url(r'^home/editprofile/$', views.editprofile, name = 'editprofile'),
		url(r'^termsofservice/$', views.termsofservice, name = 'termsofservice'),
		url(r'^privacy/$', views.privacy, name = 'privacy')
		# url(r'^home/(?P<pk>\d+)$', views.profile(model = Account) )


]