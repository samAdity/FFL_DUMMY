public class ErrorDemo {
    public static void main(String[] args) {
        String message = "Hello World";

        // This will now work without throwing a NullPointerException
        System.out.println("Message length: " + message.length());
    }
}