from setuptools import find_packages, setup

setup(
    name='earthdaily_data_processor ',
    packages = find_packages('src'),
    package_dir={"":"src"},
    version="0.0.0",
    description='Get datasets from EarthData Store and package them as datacubes.',
    author='EarthDaily Agro',
)
