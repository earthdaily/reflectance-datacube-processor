from setuptools import find_packages, setup

setup(
    name='analytics_datacube',
    packages = find_packages('src'),
    package_dir={"":"src"},
    version="0.0.1",
    description='Create an Analytics Datacube of clear images',
    author='EarthDaily Agro',
)
