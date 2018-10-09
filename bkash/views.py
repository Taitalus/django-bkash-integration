# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import utils as bkash_utils
from .models import Payment, Transaction


class PaymentCreateApiView(APIView):
    def post(self, request):
        try:
            auth_body, auth_headers = bkash_utils.get_header_body_for_token_auth()
            auth_response = requests.post(
                bkash_utils.get_bkash_app_payment_token_grant_url(),
                json=auth_body,
                headers=auth_headers
            )
            response = requests.post(
                bkash_utils.get_bkash_app_payment_create_url(),
                json=dict(request.data, **dict(currency='BDT', merchantInvoiceNumber=bkash_utils.generate_unique_id())),
                headers=bkash_utils.get_header_for_payment_create(auth_response.json().get('id_token'))
            )
            if response.status_code == 200 and response.json() and 'paymentID' in response.json():
                try:
                    payment = Payment(user=request.user, **response.json())
                    payment.save()
                except Exception as exc:
                    print(exc)
            return Response(response.json(), status=status.HTTP_200_OK)
        except Exception as exc:
            return Response(dict(
                status=500,
                message=exc.args[0]
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentExecuteApiView(APIView):
    def post(self, request):
        try:
            if 'paymentID' not in request.data:
                return Response(
                    dict(
                        status=500,
                        message='PaymentID is required'
                    ),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            auth_body, auth_headers = bkash_utils.get_header_body_for_token_auth()
            auth_response = requests.post(
                bkash_utils.get_bkash_app_payment_token_grant_url(),
                json=auth_body,
                headers=auth_headers
            )
            response = requests.post(
                '%s/%s'%(bkash_utils.get_bkash_app_payment_execute_url(), request.data.get('paymentID')),
                headers=bkash_utils.get_header_for_payment_create(auth_response.json().get('id_token'))
            )
            if response.status_code == 200 and response.json() and ('paymentID' in response.json() and 'trxID' in response.json()):
                try:
                    transaction = Transaction(user=request.user, **response.json())
                    transaction.save()
                except Exception as exc:
                    print(exc)

            return Response(response.json(), status=status.HTTP_200_OK)
        except Exception as exc:
            return Response(dict(
                status=500,
                message=exc.args[0]
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
