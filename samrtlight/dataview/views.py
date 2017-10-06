from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.views import View
from dataview.models import datalog,Area,LampInfo,RunningLog
import serial
from serial.tools import list_ports
from django.utils import timezone

def index(request):
	flag='True'
	true_flag=['True',1]   
	false_flag=['False',0]
	data={'area':Area(),
			'lampinfo': LampInfo(),
			'runninglog':RunningLog(),
			'flag':flag,
			'true_flag':true_flag}                                 # basic page for the home
	return render(request, 'dataview/home.html',data)



def serial_view():												# when called read the data from arduino if available and feeds the table
	dat=0
	available = [port[0] for port in list_ports.comports()]
	ser= serial.Serial( available[1] ,9600)
	# if ser.in_waiting!=0:
	dat=float(ser.readline().decode('ascii')) 					# get the data from the arduino
	model_obj=datalog()											# make the object of datalog table 
	model_obj.time=timezone.now()								# feed the data to the table
	model_obj.LightID=01
	model_obj.AreaID='A001'
	model_obj.current=100
	model_obj.voltage=float(dat*0.0049)
	model_obj.save()

	tag_data={  'datalog_last':datalog.objects.order_by('-id')[0] , 
				'datalog':datalog(),
				'num':dat
				 }

	return tag_data