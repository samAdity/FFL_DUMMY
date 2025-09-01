public class ErrorDemo {
    public static void main(String[] args) {
        String message = null;

        // This will throw a NullPointerException
        System.out.println("Message length: " + message.length());
    }
}
