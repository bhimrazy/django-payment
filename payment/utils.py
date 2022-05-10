import requests
from .models import Payment
from .serializers import PaymentSerializer

def esewaverifypayment(refId, amount,pk):
    import xml.etree.ElementTree as ET
    url ="https://uat.esewa.com.np/epay/transrec"
    d = {
    'amt': amount,
    'scd': 'EPAYTEST',
    'rid': refId,
    'pid':pk,
    }
    resp = requests.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    print('status',status)
    if status =="Success":
        return True
    else:
        return False

def verifypayment(token, amount):
    payload = {
        "token": token,
        "amount": amount,
    }
    headers = {
        "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
    }
    try:
        response = requests.post(settings.KHALTI_VERIFY_URL, payload,
                                 headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.HTTPError as e:
        return False


def create_payment(t_id,p_id,amt):
    """This function creates payment and return the serilized data.

    params:
    t_id: Transaction ID
    p_id: Product ID
    amt:  Total Amount
    """
    payment = Payment.objects.create(product_id=p_id,method="ESEWA",amount=amt,transaction_id=t_id)
    serializer = PaymentSerializer(payment)
    return serializer.data 