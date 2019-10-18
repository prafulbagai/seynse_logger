from setuptools import setup, find_packages

setup(name='seynse_logger',
      version='0.1.2rc1',  # version.feature.patch (rc)release-candidate 1
      url='https://bitbucket.org/SeynseDev/seynse-logging',
      license='MIT',
      author='Niranjan Singh',
      author_email='niranjan@seynse.com',
      description='Logging package to log formatted logs so that its readable via kibana, '
                  'specifically designed for seynse.',
      dependency_links=['https://pypi.deploy.loansingh.com/', ],
      packages=find_packages('.', exclude='logger_test'),
      install_requires=[
          'Django>=1.8,<2',
          'arrow>=0.12.1',
          'pytz>=2017.3',
      ],
      long_description=open('README.md').read(),
      zip_safe=False)  # As there is only one package `seynse_logger` zipping it won't effect much.