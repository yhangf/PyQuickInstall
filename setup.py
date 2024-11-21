from setuptools import setup, find_packages

VERSION = '4.0.2'

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(name='pqi',
      version=VERSION,
      description="Fast switching PyPi mirror image source",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python、PyPi source、terminal',
      author='HangfengYang',
      author_email='yhf5fhy@gmail.com',
      url='https://github.com/yhangf/PyQuickInstall',
      license='MIT',
      packages=["PQI"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'docopt',
      ],
      entry_points={
        'console_scripts':[
            'pqi = PQI.pqi:main'
        ]
      },
)
