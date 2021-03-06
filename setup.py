from setuptools import setup

setup(
    name='x100daemon',
    version='0.1.0',

    description='Make daemon for your program',
    long_description=open('README.rst').read(),
    url='https://github.com/WayneZhouChina/x100daemon',
    author='Wayne Zhou',
    author_email='cumtxhzyy@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='x100 daemon lite',

    py_modules=['x100daemon'],
    #test_suite='tests',
)
