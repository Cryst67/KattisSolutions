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
        int[] correct = {1, 1, 2, 2, 2, 8};
        int[] user = {s.nextInt(),s.nextInt(),s.nextInt(),s.nextInt(),s.nextInt(),s.nextInt()};
        for (int i = 0; i < user.length; i++) {
           System.out.print((correct[i]- user [i])+" ");
        }
    }
    
}
