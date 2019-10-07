import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spartan",
    version="0.0.1",
    author="Dean Langsam",
    author_email="deanla@gmail.com",
    description="SPARse Tools for ANalysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeanLa/spartan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)