from setuptools import setup, find_packages

setup(
    name="my_ai_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "torch", "scikit-learn", "pytest"],
)