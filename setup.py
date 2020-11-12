
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 3 - Alpha',
  'Framework :: Jupyter',
  'Intended Audience :: Developers',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries :: Python Modules',
]
 
setup(
  name='mutairibassam',
  version='0.0.1',
  description='Simplify the process of using Twitter APIs',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG').read(),
  url='https://github.com/mutairibassam/easy-twitter',  
  author='mutairibassam',
  author_email='mutairibassam@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='twitterapi', 
  packages=find_packages(),
  install_requires=[''] 
)