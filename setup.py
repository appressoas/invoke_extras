from setuptools import setup, find_packages

setup(
    name='invoke_extras',
    description='Adds functionality useful for working with Invoke.',
    version='0.0.1',
    url='https://github.com/appressoas/invoke_extras',
    author='Espen Angell Kristiansen',
    author_email='post@appresso.no',
    license='BSD',
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    install_requires=[
        'invoke',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
