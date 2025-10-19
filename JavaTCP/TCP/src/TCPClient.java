import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;


//Driver class for NIOClient
public class TCPClient {

    //Main method
    public static void main(String[] args) throws IOException {

        // Create a socket channel and connect to the server
        SocketChannel clientChannel = SocketChannel.open();
        clientChannel.connect(new InetSocketAddress("localhost", 5454));
        ByteBuffer buffer = ByteBuffer.allocate(256);
        String message = "Hello, NIO Server!";

        // Message to send to the server
        buffer.clear();
        buffer.put(message.getBytes());
        buffer.flip();

        // Send the message to the server
        while (buffer.hasRemaining()) {
            clientChannel.write(buffer);
        }
        buffer.clear();

        // Read the server's response
        clientChannel.read(buffer);
        buffer.flip();

        // Convert the response to a String and print it
        String response = new String(buffer.array(), 0, buffer.limit());
        System.out.println("Server Response: " + response);
        clientChannel.close();
    }
}