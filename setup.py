

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flatten-utils",
    version="0.1.2",
    description="CLi + module to deeply flatten nested structures like a pro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="StarCoderSC",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
    extras_require={
        "dev": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "flatten-utils = flatten_utils.cli:main",
        ],
    },
)
