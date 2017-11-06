from setuptools import setup

REQUIRED_PACKAGES = ['pandas>=0.20.3']

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    description='deepneuralnet-chess package',
)