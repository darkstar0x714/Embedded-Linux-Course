import socket

receiver_address = ('localhost', 12345)

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# try:
while True:
    try:
        message = input(
            "Enter a message to send to the receiver (or type 'exit' to quit): ")
        if message == 'exit':
            break

        sender_socket.sendto(message.encode(), receiver_address)
    except (KeyboardInterrupt):
        sender_socket.close()
        print("closed by keyboard interrupt")
        break
