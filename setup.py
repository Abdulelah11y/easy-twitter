
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

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
  name='easytwitter',
  version='0.1.1',
  description='Simplifing Twitter APIs.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/mutairibassam/easy-twitter',
  author='mutairibassam',
  author_email='mutairibassam@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='twitterapi',
  packages=find_packages(),
  install_requires=[''],
  extras_require={
    "dev": [
      "pytest>=3.7",
    ]
  }
)
