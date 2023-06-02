
import java.util.Scanner;

/**
 *
 * @author Aryan
 */
public class Test2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int win = s.nextInt();
        for (int i = 0; i < num; i++) {
            s.next();
        }
        System.out.println(win);
    }
    
}