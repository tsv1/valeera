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
    'district42==0.6.1',
    'Delorean==0.5.0'
  ],
  dependency_links=[
    'https://github.com/nikitanovosibirsk/district42/tarball/d39db770d53fd36cf62b31b55944aca719f4df71#egg=district42-0.6.1'
  ]
)
