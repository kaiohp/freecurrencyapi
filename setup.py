from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Study Project: Collect data from the FreeCurrencyAPI a Private API, process and store it in Google Cloud services (Cloud Function, Cloud Scheduler, Cloud Scret Manager and Cloud Storage).',
    author='Kaio Silva',
    license='MIT',
)