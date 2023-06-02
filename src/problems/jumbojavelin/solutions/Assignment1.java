import java.util.ArrayList;
import java.util.Scanner;

public class Assignment1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        jumbojavelin(s);
    }

    
    public static void jumbojavelin(Scanner a) {
        int num = a.nextInt();
        int list[] = new int[num];

        for (int i = 0; i < num; i++) {
            list[i] = a.nextInt();
        }
        int length = list[0];
        for (int i = 1; i < num; i++) {
            length = (list[i] + length) - 1;
        }
        System.out.println(length);
    }
}
