'''setup for pre_processing package'''

from setuptools import find_packages, setup

setup(name="preprocessing",
      version="0.1.2",
      classifiers=["Natural Language :: English",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.6"],
      description="pre-processing package for text strings",
      keywords="text pre-processing",

      url="https://github.com/mwtmurphy/pre-processing",
      author="Mitchell Murphy",
      author_email="mwtmurphy@gmail.com",
      license="MIT",

      python_requires=">=3",
      packages=find_packages(),
      package_data={
          "preprocessing": ["data/*"]
      },
      install_requires=["nltk"],
      test_suite="nose.collector",
      tests_require=["nose"],
      scripts=["bin/demo"],
      zip_safe=False)
