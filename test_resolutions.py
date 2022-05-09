import pandas as pd
import cv2

url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"
table = pd.read_html(url)[0]
table.columns = table.columns.droplevel()
cap = cv2.VideoCapture(0)
resolutions = {}
for index, row in table[["W", "H"]].iterrows():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, row["W"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, row["H"])
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    resolutions[str(width)+"x"+str(height)] = "OK"
print(resolutions)

#  Brio 4k {'160.0x120.0': 'OK', '176.0x144.0': 'OK', '320.0x180.0': 'OK', '320.0x240.0': 'OK', '424.0x240.0': 'OK',
# '340.0x340.0': 'OK', '352.0x288.0': 'OK', '480.0x270.0': 'OK', '440.0x440.0': 'OK', '640.0x360.0': 'OK',
# '640.0x480.0': 'OK', '848.0x480.0': 'OK', '800.0x600.0': 'OK', '960.0x540.0': 'OK', '1024.0x576.0': 'OK',
# '1280.0x720.0': 'OK', '1600.0x896.0': 'OK', '1920.0x1080.0': 'OK'}

#  MJPG
#  {'160.0x120.0': 'OK', '176.0x144.0': 'OK', '320.0x180.0': 'OK', '320.0x240.0': 'OK', '424.0x240.0': 'OK',
#  '352.0x288.0': 'OK', '480.0x270.0': 'OK', '640.0x360.0': 'OK', '640.0x480.0': 'OK', '848.0x480.0': 'OK',
#  '800.0x600.0': 'OK', '960.0x540.0': 'OK', '1024.0x576.0': 'OK', '1280.0x720.0': 'OK', '1600.0x896.0': 'OK',
#  '1920.0x1080.0': 'OK', '2560.0x1440.0': 'OK', '3840.0x2160.0': 'OK', '4096.0x2160.0': 'OK'}