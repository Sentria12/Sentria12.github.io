import socket

def start_tcp_client():
    # Tạo socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Thông tin server
    server_address = ('localhost', 8888)
    
    try:
        # Kết nối đến server
        print(f"🔗 Đang kết nối đến {server_address}...")
        client_socket.connect(server_address)
        print("✅ Đã kết nối thành công!")
        
        # Gửi dữ liệu
        message = "Xin chào server!".encode('utf-8')
        client_socket.sendall(message)
        print("📤 Đã gửi tin nhắn")
        
        # Nhận phản hồi
        data = client_socket.recv(1024)
        print(f"📨 Nhận được: {data.decode('utf-8')}")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
    finally:
        # Đóng kết nối
        client_socket.close()
        print("🔌 Đã đóng kết nối")

if __name__ == "__main__":
    start_tcp_client()