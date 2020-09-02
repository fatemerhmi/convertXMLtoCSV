#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='convertxmltocsv',
    version='1.0.0',
    packages=['convertxmltocsv'],
    # scripts=['xmlutils/convertxmltocsv'],
    author='Fatemeh Rahimi',
    author_email='fateme.rhmi@gmail.com',
    description='Simple tool to convert xml files to csv files',
    install_requires=[
        'setuptools',
        'pandas >= 0.22.0',
        'numpy >= 1.16.0'
    ],
    python_requires='>=3.5',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'convertxmltocsv = convertxmltocsv.convert:main'
        ]
    }
)