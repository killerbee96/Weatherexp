
from setuptools import setup, find_packages
 
setup(
    name='weather',
    version='0.1',
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['requests', 'json'],
    packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'weather = weather.weather:main'
            ]

    author='shirish dindi'
    email='myemail@example.com'
)