import setuptools
from coinpayments import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-coinpayments-sdk",
    version=version.__version__,
    author=version.__author__,
    author_email="confiyobo@gmail.com",
    description="Coinpayments SDK for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Klynox/python-coinpayments-api-wrapper",
    packages=setuptools.find_packages(),
    download_url='https://github.com/Klynox/python-coinpayments-api-wrapper/archive/v0.0.1.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "simplejson"],
)
