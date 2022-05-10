from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import esewaverifypayment,create_payment

def index(request):
    """Index route for payments"""
    return render(request,"payments/index.html")

def success(request):
    # ?q=su&oid=sdfghj-dfghjk-rtyusi&amt=100.0&refId=0003F15
    
    q,oid,amt,refId = [request.GET.get(key) for key in "q|oid|amt|refId".split("|")]

    result = esewaverifypayment(refId=refId,amount=amt,pk=oid)
    if result:
        try:
            pmt_data = create_payment(refId,oid,amt)
            # return JsonResponse({'status':"OK",'message': "Payment success",'data':pmt_data})
            print({'status':"OK",'message': "Payment success",'data':pmt_data})
            return redirect('payments_index')
        except Exception as e:
             return JsonResponse({'status':"Error",'message': str(e)})
    else:
        return redirect('esewa_failure')



def failed(request):
    
    print({'status':"Error",'message': "Payment failure",})
    return JsonResponse({'status':"Failed",'message': "Payment failure"})






# import requests as req

# url ="https://uat.esewa.com.np/epay/transrec"
# d = {
#     'amt': amt,
#     'scd': 'EPAYTEST',
#     'rid': refId,
#     'pid':oid,
# }
# resp = req.post(url, d)
# print("RESPONSE",resp.text)