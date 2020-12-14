import cv2 as cv 
import os 
import numpy as np
## cv.absdiff

def frame_diff(prev_frame, cur_frame, next_frame):

    diff_frames_1 = cv.absdiff(next_frame, cur_frame)
    diff_frames_2 = cv.absdiff(cur_frame, prev_frame)
    return_diff = cv.absdiff(diff_frames_1, diff_frames_2)
    threshold = len(return_diff[np.where(return_diff > 2)])
    if threshold > 500: print('threshold > 200 : ', threshold)
    return diff_frames_1

def get_frame(cap, scalar):
    _, frame = cap.read()
    frame = cv.resize(frame, None,fx=scalar,fy=scalar, interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    return gray

def main():
    cap = cv.VideoCapture(0)
    scaling = 0.5
    prev_frame = get_frame(cap, scaling) # Pre load for Compare Each
    cur_frame = get_frame(cap, scaling)
    next_frame = get_frame(cap, scaling)

    try:
        while True: 
            frame = frame_diff(prev_frame,cur_frame, next_frame)
            frame = cv.resize(frame,(1600,1000))
            cv.imshow('Object Movement', frame)
            prev_frame = cur_frame
            cur_frame = next_frame
            next_frame = get_frame(cap, scaling)

            if cv.waitKey(10) == ord('q'):break
    except:
        pass
        
    finally:
        cap.release()
        cv.destroyAllWindows()

main()