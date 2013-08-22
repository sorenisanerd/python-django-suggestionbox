from setuptools import setup, find_packages

setup(
    name='django-suggestionbox',
    version='0.1',
    description='Suggestion box',
    author='Soren Hansen',
    author_email='soren@linux2go.dk',
    url='http://github.com/sorenh/python-django-suggestionbox',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    keywords='suggestionbox django',
    install_requires=[
        'django',
    ],
    test_suite='tests.main',
    classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python',
     ]
)
