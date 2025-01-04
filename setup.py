from setuptools import setup, find_packages

setup(
	name="archeanvision-api",
	version="1.0.3",  # Incrémentez la version en fonction de vos mises à jour
	description="Python wrapper for the updated Archean Vision API (using Bearer Token)",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	author="Charles Hajjar",
	author_email="support@archeanvision.com",
	url="https://github.com/Archean-Vision/archeanvision-api",  # Modifiez selon votre dépôt
	packages=find_packages(),
	install_requires=[
		"requests>=2.0.0"
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)
