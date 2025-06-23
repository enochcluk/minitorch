# from setuptools import setup

# setup(py_modules=[])
from setuptools import setup, find_packages  # <- this line is critical!

setup(
    name="minitorch",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
)