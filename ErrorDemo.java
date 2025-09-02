public class ErrorDemo {
    public static void main(String[] args) {
        String message = null;

        // Check for null before accessing methods
        if (message != null) {
            System.out.println("Message length: " + message.length());
        } else {
            System.out.println("Message is null");
        }
    }
}