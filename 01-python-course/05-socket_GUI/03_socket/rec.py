import socket

receiver_address = ('localhost', 12345)

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receiver_socket.bind(receiver_address)

print("Receiver is ready to receive messages.")

try:
    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {sender_address}: {message}")

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    receiver_socket.close()
