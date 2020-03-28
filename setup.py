from setuptools import setup, find_packages
import os
from setuptools import Command


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


def create_directories():
    directories = ['/opt/influx-auto-cleaner/']
    print(f'Start creating directories: {directories}')
    for directory in directories:
        try:
            os.mkdir(directory)
            print(f'{directory} has been created')
        except FileExistsError:
            print(f'{directory} already exist')


class CustomInstallCommand(Command):
    user_options = []

    def initialize_options(self):
        """Abstract method that is required to be overwritten"""

    def finalize_options(self):
        """Abstract method that is required to be overwritten"""

    def run(self):
        create_directories()


tests_require = [],

setup(
    name='influx-auto-cleaner',
    packages=find_packages(),
    version='0.0.1',
    license='Apache License 2.0',
    description='Remove some InfluxDB tags automatically if data point was not inserted during specific period of time',
    url='https://github.com/howlets/influxdb_auto_cleaner',
    author='Mykola Kondratiuk',
    author_email='howlets.io@gmail.com',
    download_url='https://github.com/howlets/influxdb_auto_cleaner/archive/0.0.1.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.6'
    ],
    setup_requires=[
        'pytest-runner',
        'flake8'
    ],
    keywords=['influxdb', 'cleaner'],
    install_requires=requirements,
    tests_require=tests_require,
    entry_points={
        'console_scripts': ['influx-auto-cleaner = auto_cleaner.__main__:main']
    },
    zip_safe=False,
    include_package_data=True,
    cmdclass={'prepare': CustomInstallCommand},
    data_files=[
        ('/opt/influx-auto-cleaner', ['config.yaml'])
    ]
)