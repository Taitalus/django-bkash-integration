from django.db import models
from .managers import PaymentManager, TransactionManger
# Create your models here.
'''
{
    "paymentID": "13HYFS31539088469895",
    "createTime": "2018-10-09T12:34:29:962 GMT+0000",
    "orgLogo": "https://s3-ap-southeast-1.amazonaws.com/merchantlogo.sandbox.bka.sh/merchant-default-logo.png",
    "orgName": "TestDemoMerchant",
    "transactionStatus": "Initiated",
    "amount": "100",
    "currency": "BDT",
    "intent": "sale",
    "merchantInvoiceNumber": "od8ZBmQx4nA"
}
'''
from django.conf import settings
from model_utils.models import TimeStampedModel, SoftDeletableModel, SoftDeletableManager
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')


class Payment(TimeStampedModel, SoftDeletableModel):
    paymentID = models.CharField(max_length=50, unique=True, editable=False, primary_key=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments'
    )
    createTime = models.TextField()
    orgLogo = models.URLField(max_length=250)
    orgName = models.CharField(max_length=100)
    transactionStatus = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    currency = models.CharField(max_length=20)
    intent = models.CharField(max_length=20)
    merchantInvoiceNumber = models.CharField(max_length=30)

    objects = PaymentManager()
    soft_manager = SoftDeletableManager()

    class Meta:
        db_table = 'payments'
        ordering = ('-created', )




'''
{
    'paymentID': 'OFN3R7S1539093934542',
    'createTime': '2018-10-09T14:05:34:643 GMT+0000',
    'updateTime': '2018-10-09T14:06:20:600 GMT+0000',
    'trxID': '5J93015CSH',
    'transactionStatus': 'Completed',
    'amount': '17.29',
    'currency': 'BDT',
    'intent': 'sale',
    'merchantInvoiceNumber': 'WqDJJMDxVMa'
}
'''


class Transaction(TimeStampedModel, SoftDeletableModel):
    paymentID = models.CharField(max_length=50)
    createTime = models.TextField()
    updateTime = models.TextField()
    trxID = models.CharField(max_length=50, primary_key=True, editable=False, unique=True)
    transactionStatus = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    intent = models.CharField(max_length=20)
    merchantInvoiceNumber = models.CharField(max_length=30)
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions'
    )

    objects = TransactionManger()
    soft_manager = SoftDeletableManager()

    class Meta:
        db_table = 'transactions'
        ordering = ('-created', )
