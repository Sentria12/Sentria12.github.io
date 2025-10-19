import socket

def start_tcp_server():
    # Tạo socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind địa chỉ và port
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)
    
    # Lắng nghe kết nối (tối đa 5 kết nối chờ)
    server_socket.listen(5)
    print(f"🚀 Server đang lắng nghe trên {server_address}")
    
    try:
        while True:
            # Chấp nhận kết nối từ client
            print("⏳ Đang chờ kết nối...")
            client_socket, client_address = server_socket.accept()
            print(f"✅ Đã kết nối với {client_address}")
            
            try:
                # Nhận dữ liệu từ client
                data = client_socket.recv(1024)
                print(f"📨 Nhận được: {data.decode('utf-8')}")
                
                # Gửi phản hồi
                response = "Xin chào từ server!".encode('utf-8')
                client_socket.sendall(response)
                print(" Đã gửi phản hồi")
                
            finally:
                # Đóng kết nối với client
                client_socket.close()
                print(f"🔌 Đã đóng kết nối với {client_address}\n")
                
    except KeyboardInterrupt:
        print("\n🛑 Server dừng hoạt động")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()