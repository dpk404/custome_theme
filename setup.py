from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_theme/__init__.py
from custom_theme import __version__ as version

setup(
	name="custom_theme",
	version=version,
	description="Customized theme for ERPNext/Frappe",
	author="Deepak",
	author_email="dk950046@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
