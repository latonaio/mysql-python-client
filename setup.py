#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name='mysql-python-client',
	version='0.1.0',
	description='mysql client',
	long_description='mysql client',
	packages=['mysql_client'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'mysqlclient==2.0.3',
	],
	entry_points='''
''')