public class ErrorDemo {
    public static void main(String[] args) {
        String message = null;

        // Fixed: Check for null before calling length()
        if (message != null) {
            System.out.println("Message length: " + message.length());
        } else {
            System.out.println("Message length: 0 (message is null)");
        }
    }
}