"""
Author: Raju Ahmed Shetu
"""
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bkash-integration',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple django app to integrate bkash rest api to your application',
    long_description=README,
    url='https://github.com/Taitalus/django-bkash-integration',
    author='Raju Ahmed Shetu',
    author_email='shetu2153@gmail.com',
    install_requires=[
        'django>=2.0',
        'djangorestframework>=3.8',
        'hashids>=1.2',
        'requests>=2.19'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
