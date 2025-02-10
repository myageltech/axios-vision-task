import argparse
from src.streamer.streamer import Streamer
from src.detector.detector import Detector
from src.view.view import View
import cv2
import time

def main(video_path, no_blurrings):
    streamer = Streamer(video_path)
    detector = Detector()
    view = View()
    show = True
    while show:
        # Get frame from streamer
        frame = streamer.get_frame()
        if frame is None:
            break
        # Use frame and analyze it via detector
        processed_frame, detections = detector.analyze_frame(frame)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # If no_blurrings is true, display without blurring; otherwise, use the blurring feature
        view.display_frame(processed_frame, detections, current_time, no_blurrings)
        
        # my own feature to kill the the processes and exit window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            view.close()
            cv2.destroyAllWindows()
            show = False
    
    streamer.release()
    view.close()
    cv2.destroyAllWindows()  #step3

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video Stream Analytics")
    parser.add_argument("--input-file", type=str, default="src/data/People-6387.mp4", help="Path to the input video file")
    parser.add_argument("--no-blurrings", action="store_true", help="Disable blur on detected regions")
    args = parser.parse_args()

    main(args.input_file, args.no_blurrings)