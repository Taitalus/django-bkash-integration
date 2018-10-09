"""
Author: Raju Ahmed Shetu
"""
import math
import time
import string
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from hashids import Hashids


def get_bkash_app_key(key='BKASH_APP_KEY'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_secret(key='BKASH_APP_SECRET'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_username(key='BKASH_APP_USERNAME'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_password(key='BKASH_APP_PASSWORD'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_version(key='BKASH_APP_VERSION'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_base_url(key='BKASH_APP_BASE_URL'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_payment_create_url(key='BKASH_APP_PAYMENT_CREATE_URL'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_payment_token_grant_url(key='BKASH_APP_PAYMENT_TOKEN_GRANT_URL'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_bkash_app_payment_execute_url(key='BKASH_APP_PAYMENT_EXECUTE_URL'):
    try:
        return getattr(settings, key)
    except ImproperlyConfigured as exc:
        raise ImproperlyConfigured('%s is not set' % key)


def get_header_body_for_token_auth():
    token_headers = dict(
        username=get_bkash_app_username(),
        password=get_bkash_app_password()
    )

    token_body = dict(
        app_secret=get_bkash_app_secret(),
        app_key=get_bkash_app_key()
    )
    return token_body, token_headers


def get_header_for_payment_create(token: str):
    return {
        'X-APP-Key': get_bkash_app_key(),
        'Authorization': token
    }


def get_hashid_object():
    hashid = Hashids(
        min_length=8,
        alphabet=string.ascii_uppercase + string.ascii_lowercase + string.digits,
        salt=get_bkash_app_key(),
    )
    return hashid


def generate_unique_id():
    t = time.time() * math.pow(10, 6)
    return get_hashid_object().encode(int(t))
