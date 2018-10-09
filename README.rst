=========================
Bkash Django Integration
=========================

Bkash Django Integration app is to integrate Bkash Api to Django Backend. With Minimal setup in the `settings.py`, one can easily perform bkash checkout api and store response from bkash api for further audit issues

Detailed documentation is in the "docs" directory.

Installation
------------
``` pip install django-bkash-integration ```

Quick start
-----------

1. Add "bkash" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bkash',
    ]

2. Include the bkash URLconf in your project urls.py like this::

    path('bkash/', include('bkash.urls')),

3. Define the following constants in the version settings.py::

    BKASH_APP_KEY = // bkash app key
    BKASH_APP_SECRET = // bkash app secret
    BKASH_APP_USERNAME = // bkash app username
    BKASH_APP_PASSWORD = // bkash app password
    BKASH_APP_VERSION = // bkash app version
    BKASH_APP_BASE_URL = // bkash app base url
    BKASH_APP_PAYMENT_TOKEN_GRANT_URL = '%s/%s/checkout/token/grant' % (BKASH_APP_BASE_URL, BKASH_APP_VERSION)
    BKASH_APP_PAYMENT_CREATE_URL = '%s/%s/checkout/payment/create' % (BKASH_APP_BASE_URL, BKASH_APP_VERSION)
    BKASH_APP_PAYMENT_EXECUTE_URL = '%s/%s/checkout/payment/execute' % (BKASH_APP_BASE_URL, BKASH_APP_VERSION)

4. Make sure you have postgres database and the routes are protected by some kind of oauth2 authentication

5. Run `python manage.py migrate` to create the bkash models.

6. Host the application in a remote server and connect from the frontend.

7. For any query and bug please file an issue or knock me at shetu2153@gmail.com

Happy Coding !!!
