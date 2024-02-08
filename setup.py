'''setup for pre_processing package'''

from setuptools import find_packages, setup

def get_requirements():
    '''returns requirements array for package'''
    packages = []
    with open("requirements.txt", "r") as req_doc:
        for package in req_doc:
            packages.append(package.replace("\n", ""))
    return packages

setup(name="preprocessing",
    version="0.1.12",
    classifiers=["Natural Language :: English",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.6"],
    description="pre-processing package for text strings",
    long_description=open("README.rst").read(),
    keywords="text pre-processing",

    url="https://github.com/SpotlightData/preprocessing",
    author="Mitchell Murphy",
    author_email="mwtmurphy@gmail.com",
    license="MIT",

    python_requires=">=3",
    packages=find_packages(),
    package_data={
        "preprocessing": [
            "data/**"
        ]
    },
    include_package_data=True,

    install_requires=get_requirements(),

    test_suite="nose.collector",
    tests_require=["nose"],
    scripts=["bin/demo"],
    zip_safe=False)
