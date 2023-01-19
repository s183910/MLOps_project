import requests
import cv2

# Make a post request to the API

base_url = "https://model-inference-main-aa4gpdvyka-no.a.run.app/"
upload = "upload_img/"

def stream():
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame if key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        _, frame = video_capture.read()
        _, img_encoded = cv2.imencode('.png', frame)
        img_bytes = img_encoded.tobytes()
        cv2.imshow('Video', frame)

        files = [('files', img_bytes)]

        # Make a post request to the API
        response = requests.post(base_url + upload, files=files)
        
        print("letter:",response.json()[0]["classification"])

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    stream()