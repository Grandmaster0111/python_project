import qrcode 
from PIL import Image
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data('https://www.pcgamingworld.co.in/search/label/Action')
qr.make(fit=True)
# img = qr.make('https://www.pcgamingworld.co.in/search/label/Action') 
# img.save('pc_game_download.png')
img=qr.make_image(fill_color='green',back_color='white')
img.save('pc_game_download.png')