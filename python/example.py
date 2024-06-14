import utils
import socket
import cv2

#first run matlab program -> "streamNaneyeImage('127.0.0.1', 8888)"

ip = "127.0.0.1"
port = 8888
nbytes = 250000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(ip, port)
    print("Successfully Connected")

    while True:
        try:
            data = utils.readnbytes(sock, 250000)

            frame = utils.convertToImage(data)

            cv2.imshow("image", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                sock.close()
                break
        except Exception as e:
            print(e)
            break

    cv2.destroyAllWindows()
