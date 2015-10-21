from codecs import open
from distutils.core import setup

setup(name='hashfield',
      version='0.1.2',
      packages=['hashfield'],
      license='MIT',
      include_package_data=True,
      author='EgemSoft',
      author_email='info@egemsoft.net',
      url='https://github.com/egemsoft/django-hashfield',
      description='A reusable Django field.',
      long_description=open("README.rst").read(),
      install_requires=['Django >= 1.4.3'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Framework :: Django',
      ],
      )
