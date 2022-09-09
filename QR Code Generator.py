import qrcode
# import qrcode library

def generate_qrcode(text):
    # QRCode() is used to specify the settings we wanna make to qrcode
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=3.5)
    # Passes our string to the qr code
    qr.add_data(text)
    qr.make(fit=True)
    # Color choosing
    img = qr.make_image(fill_color='white', back_color='black')
    # Saving the file finally
    img.save('qrcode.png')


while True:
    url = input('\nEnter url: ')
    generate_qrcode(url)
    print('The Qrcode has been saved')
