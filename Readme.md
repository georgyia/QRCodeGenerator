# QR Code Generator

This is a simple command-line tool for generating QR codes.

## Setup

1. Ensure you have Python 3 installed. You can download it from the official website.

2. Install the required Python packages. You can do this by running the following command:

```
/usr/local/bin/python3 -m pip install qrcode
```

## Usage

You can generate a QR code by running the qrcodegenerator.py script with the following arguments:

- data: The data to encode in the QR code. This is a required argument.
- output: The output file name. This is a required argument.
- --box_size: The size of each box in the QR code. The default is 10.
- --border: The size of the border around the QR code. The default is 5.
- --error_correction: The level of error correction. This determines how much of the QR code can be damaged or obscured while still being readable. The options are 'L', 'M', 'Q', and 'H'. The default is 'M'.
- --fill_color: The color of the QR code. The default is 'black'.
- --back_color: The background color of the QR code. The default is 'white'.

Here's an example command:

```
/usr/local/bin/python3 qrcodegenerator.py "https://de.wikipedia.org/wiki/Munich" qrcode.png --box_size 10 --border 5 --error_correction H --fill_color black --back_color white
```

This command generates a QR code that encodes the URL "https://de.wikipedia.org/wiki/Munich". The QR code has a box size of 10, a border size of 5, a high level of error correction ('H'), a black fill color, and a white background color. The QR code is saved to the file qrcode.png.

## Examples

Here are some examples of QR codes you can generate:

- A QR code that encodes the text "Hello, world!":

```
/usr/local/bin/python3 qrcodegenerator.py "Hello, world!" hello_world.png
```

- A QR code that encodes a URL and has a high level of error correction:

```
/usr/local/bin/python3 qrcodegenerator.py "https://www.example.com" example.png --error_correction H
```

- A QR code with custom colors:

```
/usr/local/bin/python3 qrcodegenerator.py "https://www.example.com" example.png --fill_color blue --back_color yellow
```

---

Remember to replace /usr/local/bin/python3 with the path to your Python interpreter if it's different.