# import required libraries
from vidgear.gears import VideoGear
import cv2
import numpy as np
import time

# define suitable tweak parameters for your stream.
options = {
    "CAP_PROP_FRAME_WIDTH": 1920,  # resolution 320x240
    "CAP_PROP_FRAME_HEIGHT": 1080,
    "CAP_PROP_FPS": 60,  # frame rate 60fps
    "CAP_PROP_AUTOFOCUS": 0,
    "CAP_PROP_FOCUS": 0,
}

# define and start the stream on first source ( For e.g #0 index device)
stream1 = VideoGear(source=0, logging=True, **options).start()

# define and start the stream on second source ( For e.g #1 index device)
#stream2 = VideoGear(source=2, logging=True).start()

# define and start the stream on second source ( For e.g #1 index device)
#stream3 = VideoGear(source=1, logging=True, **options).start()

# define and start the stream on second source ( For e.g #1 index device)
#stream4 = VideoGear(source=2, logging=True, **options).start()

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

# infinite loop
while True:

    frameA = stream1.read()
    # read frames from stream1

    #frameB = stream2.read()
    # read frames from stream2

    #frameC = stream3.read()
    # read frames from stream2

    #frameD = stream4.read()
    # read frames from stream2

    # check if any of two frame is None
    #if frameA is None or frameB is None:
    #    # if True break the infinite loop
    #    break

    # font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    # time when we finish processing for this frame
    new_frame_time = time.time()

    # Calculating the fps

    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # converting the fps into integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)

    # putting the FPS count on the frame
    cv2.putText(frameA, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    # do something with both frameA and frameB here
    cv2.imshow("Output Frame1", frameA)
    #cv2.imshow("Output Frame2", frameB)
    #cv2.imshow("Output Frame3", frameC)
    #cv2.imshow("Output Frame4", frameD)
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
        #cv2.imwrite("Image-3.jpg", frameC)
        #cv2.imwrite("Image-4.jpg", frameD)
        # break   #uncomment this line to break out after taking images

cv2.destroyAllWindows()
# close output window

# safely close both video streams
stream1.stop()
#stream2.stop()
#stream3.stop()
#stream4.stop()
