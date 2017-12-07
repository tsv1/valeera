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
    'https://github.com/nikitanovosibirsk/district42/tarball/9c25d60a2082dd266e3251dec529a2334bf24300#egg=district42-0.6.1'
  ]
)
