public class ErrorDemo {
    public static void main(String[] args) {
        String message = null;

        // Check for null before using the string
        if (message != null) {
            System.out.println("Message length: " + message.length());
        } else {
            System.out.println("Message is null");
        }
    }
}