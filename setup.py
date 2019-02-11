import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skeddly-sdk",
    version="1.0.0",
    author="Eleven41 Software Inc.",
    author_email="support@skeddly.com",
    description="Skeddly SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eleven41/skeddly-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)