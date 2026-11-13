"""Generate an actual scannable QR for the *published* Cuelshii viewer URL.
Usage: python make_qr.py https://YOURUSERNAME.github.io/cuelshii-360/
Requires: pip install qrcode[pil]
"""
import sys
try:
    import qrcode
except ImportError:
    print('Please run: pip install "qrcode[pil]"')
    sys.exit(1)
from pathlib import Path
from urllib.parse import urlparse
if len(sys.argv) < 2 or not sys.argv[1].startswith('https://'):
    print('Usage: python make_qr.py https://YOUR-PUBLIC-WEBSITE-URL/')
    sys.exit(2)
url = sys.argv[1].strip()
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
q.add_data(url)
q.make(fit=True)
img = q.make_image(fill_color='#403044', back_color='#FFFFFF').convert('RGB')
output = Path(__file__).parent/'Cuelshii_QR_360.png'
img.save(output, dpi=(300,300))
print(f'Generated: {output} ({img.width} x {img.height}) → {url}')
