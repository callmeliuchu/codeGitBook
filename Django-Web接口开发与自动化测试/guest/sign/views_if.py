from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist


def add_event(request):
	eid = request.POST.get('eid','')
	name = request.POST.get('name','')
	limit = request.POST.get('limit','')
	status = request.POST.get('status','')
	address = request.POST.get('address','')
	start_time = request.POST.get('start_time','')
	if eid == ''  or name == '' or limit == '' or address == ''  or start_time == '':
		return JsonResponse({'status':10021,'message':'parameter error'})
	result = Event.objects.filter(id=eid)
	if result:
		return JsonResponse({'status':10022,'message':'event id already exists'})
	result = Event.objects.filter(id=name)
	if result:
		return JsonResponse({'status':10023,'message':'event name already exists'})
	if status == '':
		status = 1
	try:
		Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
	except ValidationError as e:
		error = 'date format must be YYYY-MM-DD HH:MM:SS'
		return JsonResponse({'status':1004,'message':error})
	return JsonResponse({'status':200,'message':'add event success'})


def get_event_list(request):
	eid = request.GET.get("eid","")
	name = request.GET.get("name","")

	if eid == '' and name == '':
		return JsonResponse({'status':10021,'message':'parameter error'})

	if eid != '':
		event = {}
		try:
			result = Event.objects.get(id=eid)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022,'message':'query result is empty'})
		else:
			event['name'] = result.name
			event['limit'] = result.limit
			event['status'] = result.status
			event['address'] = result.address
			event['start_time'] = result.start_time
			return JsonResponse({'status':200,'message':'success','data':event})
	if name != '':
		datas = []
		results = Event.objects.filter(name=name)
		if results:
			for r in results:
				event = {}
				event['name']=r.name
				event['limit']=r.limit
				event['status']=r.status
				event['address']=r.address
				event['start_time']=r.start_time
				datas.append(event)
			return JsonResponse({'status':200,'message':'success','data':datas})
		else:
			return JsonResponse({'status':10022,'message':'query result is empty'})



