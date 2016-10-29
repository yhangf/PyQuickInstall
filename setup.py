from setuptools import setup, find_packages

VERSION = '1.0.2'

setup(name='pqi',
      version=VERSION,
      description="Fast switching PyPi mirror image source",
      long_description='just convenient',
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python、PyPi source、terminal',
      author='Yanghangfeng',
      author_email='1437183653@qq.com',
      url='https://github.com/Fenghuapiao/PyQuickInstall',
      license='MIT',
      packages=["PQI"],
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
