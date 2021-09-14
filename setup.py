import setuptools
from pycoinpayments import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycoinpayments",
    version=version.__version__,
    author=version.__author__,
    author_email="confiyobo@gmail.com",
    description="Coinpayments SDK for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Klynox/python-coinpayments-api-wrapper",
    packages=setuptools.find_packages(),
    download_url='https://github.com/Klynox/python-coinpayments-api-wrapper/archive/v{0}.tar.gz'.format(
        version.__version__),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        'wrapper',
        'sdk',
        'coinpayments',
        'coinpayments-sdk',
        'coinpayments-api-wrapper'
    ],
)
