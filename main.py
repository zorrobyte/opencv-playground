# import required libraries
from vidgear.gears import VideoGear
import cv2

# define suitable tweak parameters for your stream.
options = {
    "CAP_PROP_FRAME_WIDTH": 853,  # resolution 320x240
    "CAP_PROP_FRAME_HEIGHT": 480,
    "CAP_PROP_FPS": 20,  # frame rate 60fps
    "CAP_PROP_AUTOFOCUS": 0,
    "CAP_PROP_FOCUS": 0,
}

# define and start the stream on first source ( For e.g #0 index device)
stream1 = VideoGear(source=0, logging=True, **options).start()

# define and start the stream on second source ( For e.g #1 index device)
#stream2 = VideoGear(source=1, logging=True).start()

# define and start the stream on second source ( For e.g #1 index device)
stream3 = VideoGear(source=2, logging=True, **options).start()

# define and start the stream on second source ( For e.g #1 index device)
stream4 = VideoGear(source=3, logging=True, **options).start()

# infinite loop
while True:

    frameA = stream1.read()
    # read frames from stream1

    #frameB = stream2.read()
    # read frames from stream2

    frameC = stream3.read()
    # read frames from stream2

    frameD = stream4.read()
    # read frames from stream2

    # check if any of two frame is None
    if frameA is None or frameC is None:
        # if True break the infinite loop
        break

    # do something with both frameA and frameB here
    cv2.imshow("Output Frame1", frameA)
    #cv2.imshow("Output Frame2", frameB)
    cv2.imshow("Output Frame3", frameC)
    cv2.imshow("Output Frame4", frameD)
    # Show output window of stream1 and stream 2 separately

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        # if 'q' key-pressed break out
        break

    if key == ord("w"):
        # if 'w' key-pressed save both frameA and frameB at same time
        cv2.imwrite("Image-1.jpg", frameA)
        #cv2.imwrite("Image-2.jpg", frameB)
        cv2.imwrite("Image-3.jpg", frameC)
        cv2.imwrite("Image-4.jpg", frameD)
        # break   #uncomment this line to break out after taking images

cv2.destroyAllWindows()
# close output window

# safely close both video streams
stream1.stop()
#stream2.stop()
stream3.stop()
stream4.stop()
