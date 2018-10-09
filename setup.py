from setuptools import find_packages, setup

setup(
  name='valeera',
  description='Validator for district42 schema',
  version='0.6.3',
  url='https://github.com/nikitanovosibirsk/valeera',
  author='Nikita Tsvetkov',
  author_email='nikitanovosibirsk@yandex.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[
    'district42==0.6.3',
    'Delorean==0.5.0'
  ],
  dependency_links=[
    'https://github.com/nikitanovosibirsk/district42/tarball/e81ef1fc033e47a94b9101b05981b73a722aa1ed#egg=district42-0.6.3'
  ]
)
