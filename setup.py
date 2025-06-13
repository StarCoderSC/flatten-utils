from setuptools import setup, find_packages

setup(
    name="flatten-utils",
    version="0.1.0",
    description="Deep flatten nested structures like a pro",
    author="StarCoder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "flatten-utils = flatten_utils.cli:main",
        ],
    },
)
