public class ErrorDemo {
    public static void main(String[] args) {
        String message = null;

        if (message != null) {
            System.out.println("Message length: " + message.length());
        } else {
            System.out.println("Message is null, cannot get length");
        }
    }
}