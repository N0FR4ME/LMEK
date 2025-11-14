from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lmek",
    version="0.1.0",
    author="N0FR4ME",
    description="Calculator with graphing/plotting functionality for linear mathematic analysis and electrical circuits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "scipy>=1.10.0",
        "sympy>=1.12",
    ],
)
