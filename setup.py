from setuptools import setup

setup(
    name="mtg-price-check",
    version="1.0",
    description="Easy way to price check Magic the Gathering cards.",
    author="Jeremy Ng",
    author_email="jeremy1x.ng@intel.com",
    packages=["mtg-price-check"],
    package_dir={"mtg-price-check": "src"},
    # external packages as dependencies
    install_requires=["mtg-price-check", "opencv-python", "pytesseract"],
)
