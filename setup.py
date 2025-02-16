from setuptools import setup, find_packages 


setup(
  name = 'condor_src',         # How you named your package folder (MyLib)
  version = '0.1.0',
  license='MIT',
  description = 'A HTCondor library for python',
  author = 'Yue Ma',
  author_email = 'mayueanyou@gmail.com',
  packages=find_packages(),
  url = 'https://github.com/mayueanyou/condor_src', 
)