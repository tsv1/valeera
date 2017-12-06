from setuptools import find_packages, setup

setup(
  name='valeera',
  description='Validator for district42 schema',
  version='0.6.1',
  url='https://github.com/nikitanovosibirsk/valeera',
  author='Nikita Tsvetkov',
  author_email='nikitanovosibirsk@yandex.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[
    'district42==0.6.2',
    'Delorean==0.5.0'
  ],
  dependency_links=[
    'https://github.com/nikitanovosibirsk/district42/tarball/d445f0e57bfa8d37b6dd3428573832d150e6bc6c#egg=district42-0.6.1'
  ]
)
