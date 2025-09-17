# LinkedIn Profile 
linkedin_url= "https://www.linkedin.com/in/quatazia-johnson-79b039243"

#Generate QR Code

# Import required libraries
import qrcode
from PIL import Image
import requests
from io import BytesIO

# Define color scheme
MAROON = (128, 0, 32)
STEEL = (70, 130, 180)

# Generate QR code for LinkedIn profile
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=10,
	border=4,
)
qr.add_data(linkedin_url)
qr.make(fit=True)

# Create an image from the QR Code instance with custom colors
img = qr.make_image(fill_color=MAROON, back_color=STEEL).convert('RGB')

# Download and process the school logo
logo_url = "https://www.pikpng.com/pngl/b/471-4718219_university-of-virginia-logo-png.png"
response = requests.get(logo_url)
logo = Image.open(BytesIO(response.content)).convert("RGBA")

# Resize logo to fit in the center of the QR code
qr_width, qr_height = img.size
logo_size = int(qr_width * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate position and paste logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
img.paste(logo, pos, mask=logo)

# Save the image to a file
img.save("linkedin_qr.png")