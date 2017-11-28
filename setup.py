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
    'https://github.com/nikitanovosibirsk/district42/tarball/2c85670bdadf7d7caa1de4b438c1399919c5487b#egg=district42-0.6.1'
  ]
)
