

# flatten-utils
[![PyPI version](https://badge.fury.io/py/flatten-utils.svg)](https://pypi.org/project/flatten-utils/)

[![Downloads](https://static.pepy.tech/badge/flatten-utils)](https://pepy.tech/project/flatten-utils)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)


🔧 A lightweight utility to deeply flatten nested Python structure like 'lists', 'tuples', 'sets','dicts' and more -- without breaking a sweat.

## 🚀 Features 

- 🌀 Deep flattening of arbitrarily nested structures
- 🔂 Control flatten depth with '--depth'
- ➖ Stop flattening at specific types like 'str', 'bytes', 'dict' with '--stop_at'
- 📦 Use as both an **Python module** and a *CLI tool*
- 📁 Read Input from files or strings
- 🎨 Pretty-printing support with '--pretty'

## Usage Example

### As a CLI tool:

'''bash
flatten-utils "[1, [2, [3, 4]]]"
# Output: [1, 2, 3, 4]

flatten-utils --file input.json --depth 2 --pretty


## 📦 Installation

### ✅ From PYPI (recommended)

```bash
pip install flatten-utils



