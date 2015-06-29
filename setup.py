from distutils.core import setup


setup(name='hashfield',
    version='0.1.1',
    packages=['hashfield'],
    license='MIT',
    include_package_data=True,
    author='Hasan Basri Ates',
    author_email='hbasria@gmail.com',
    url='https://github.com/hbasria/django-hashfield/',
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