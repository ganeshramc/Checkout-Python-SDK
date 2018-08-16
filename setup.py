import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonrestsdk",
    version="0.0.2.1",
    author="Ganeshram Chockalingam",
    author_email="ganeshramc@live.com",
    description="Python Rest SDK for Checkout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.paypal.com/gchockalingam/Checkout-python-SDK/",
    packages=setuptools.find_packages(),
    install_requires=['braintreehttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)