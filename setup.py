from setuptools import setup, find_packages

setup(name='seynse_logger',
      version='0.1.2rc1',  # version.feature.patch (rc)release-candidate 1
      url='https://bitbucket.org/SeynseDev/seynse-logging',
      license='MIT',
      author='Niranjan Singh',
      author_email='niranjan@seynse.com',
      description='Logging package to log formatted logs so that its readable via kibana, '
                  'specifically designed for seynse.',
      install_requires=[
            'arrow==0.16.0',
            'pytz==2020.1'
      ],
      packages=find_packages('.', exclude='logger_test'),
      long_description=open('README.md').read(),
      zip_safe=False)  # As there is only one package `seynse_logger` zipping it won't effect much.
