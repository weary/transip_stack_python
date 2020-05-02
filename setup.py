from setuptools import setup

setup(name='transip_stack_webdav',
      version='0.1.0',
      install_requires=[
          'webdavclient3',
      ],
      entry_points={
          'console_scripts': [
              'transip_upload = webdavtest:upload',
          ]
      },
      )
