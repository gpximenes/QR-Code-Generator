Great! Since you have a `.requirements` file in your project, I'll include a section in the README that details how to install these dependencies. Here is the complete README file for your QR code generator project:

---

# QR Code Generator

## Introduction
This Python script, `QR_Generator.py`, is a tool for generating and saving QR codes. It uses the `segno` library to create QR codes from input text and provides functionalities for saving these QR codes as PNG files, with options to specify the filename and scale.

## Table of Contents
- Introduction
- Installation
- Usage
- Features
- Dependencies
- Configuration
- Examples


## Installation
To use this script, ensure you have Python installed on your system. The dependencies for the script are listed in the `.requirements` file. Install them using pip:

```bash
pip install -r .requirements
```

## Usage

To use `QR_Generator.py`, run it from the command line with the required and optional arguments as follows:

```bash
python QR_Generator.py QR_TEXT [--filename FILENAME] [--scale SCALE]
```

### Arguments
- `QR_TEXT` (required): The text you want to encode in the QR code.
- `--filename` or `--fn` (optional): Name of the output file. If not provided, the script generates a filename in the format `QR_code_[N].png`.
- `--scale` or `--s` (optional): Scale of the QR code image. The default scale is 10.

### Examples
To generate a QR code with default settings:
```bash
python QR_Generator.py "Example Text"
```

To generate a QR code with a specific filename and scale:
```bash
python QR_Generator.py "Example Text" --filename "MyQRCode" --scale 5
```

## Features
- Generate QR codes from text.
- Save QR codes as PNG files.
- Option to specify the filename for the saved QR code.
- Ability to set the scale of the QR code.

## Dependencies
- Python
- segno

