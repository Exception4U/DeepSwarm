import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepswarm",
    version="0.0.1",
    author="Edvinas Byla",
    author_email="edvinasbyla@gmail.com.com",
    description="Neural Architecture Search Powered by Swarm Intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pattio/DeepSwarm",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama==0.4.1',
        'pyyaml==3.13',
        'scikit-learn==0.20.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)