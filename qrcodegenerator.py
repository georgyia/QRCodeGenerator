import qrcode
import argparse
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

# Create the command line argument parser
parser = argparse.ArgumentParser(description='Generate a QR code.')
parser.add_argument('data', help='The data to encode in the QR code')
parser.add_argument('output', help='The output file name')
parser.add_argument('--box_size', type=int, default=10, help='The size of each box in the QR code')
parser.add_argument('--border', type=int, default=5, help='The size of the border around the QR code')
parser.add_argument('--error_correction', choices=['L', 'M', 'Q', 'H'], default='M', help='The level of error correction')
parser.add_argument('--fill_color', default='black', help='The color of the QR code')
parser.add_argument('--back_color', default='white', help='The background color of the QR code')

# Parse the command line arguments
args = parser.parse_args()

# Map the error correction argument to the corresponding constant
error_correction = {
    'L': ERROR_CORRECT_L,
    'M': ERROR_CORRECT_M,
    'Q': ERROR_CORRECT_Q,
    'H': ERROR_CORRECT_H,
}[args.error_correction]

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=error_correction,
    box_size=args.box_size,
    border=args.border,
)
qr.add_data(args.data)
qr.make(fit=True)
img = qr.make_image(fill=args.fill_color, back_color=args.back_color)

# Save the QR code to a file
img.save(args.output)