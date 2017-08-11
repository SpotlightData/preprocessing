'''setup for pre_processing package'''

from setuptools import find_packages, setup

def get_readme():
    '''returns readme for package'''
    with open("README.md", "r") as readme_doc:
        return readme_doc.read()

setup(name="pre_processing",
      version="0.1.1",
      classifiers=["Natural Language :: English",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.6"],
      description="pre-processing package for text strings",
      long_description=get_readme(),
      keywords="text pre-processing",

      url="https://github.com/mwtmurphy/pre-processing",
      author="mwtmurphy",
      license="MIT",

      python_requires=">=3",
      packages=find_packages(),
      package_data={
          "pre_processing": ["data/*"]
      },
      install_requires=["nltk"],
      test_suite="nose.collector",
      tests_require=["nose"],
      scripts=["bin/demo"],
      zip_safe=False)
