import siaskynet
import pyscreenshot as ImageGrab
import pathlib
from datetime import datetime
import time
import webbrowser

blurb_generating_screencap = 'Generating your screen capture...'
blurb_saved_locally = 'Your screenshot has been saved locally as: '
blurb_current_directoy = 'You will find it at the current directory: '
blurb_uploading_image = 'Now uploading the screenshot to Skynet...'
blurb_description = 'This is the Skylink that you can share with anyone to retrieve the file on any Skynet Webportal:'
blurb_url = 'Please check at the following link: '
blurb_host = 'https://siasky.net/'

now = datetime.now()
timestamp = str(int(datetime.timestamp(now)))

print(blurb_generating_screencap)
screenshot = ImageGrab.grab()
screenshot.save('screenshot_' + timestamp + '.png')
path_to_screenshot = pathlib.Path().absolute()
print(blurb_current_directoy + str(path_to_screenshot))
print()
print(blurb_uploading_image)
print(blurb_description)
skylink = siaskynet.Skynet.UploadFile('screenshot_' + timestamp + '.png', None)
print(skylink)
print()
url_link = blurb_host + skylink[6:]
print(blurb_url + url_link)
time.sleep(2)
webbrowser.open_new(url_link)
