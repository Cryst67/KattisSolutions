import java.util.ArrayList;
import java.util.Scanner;

public class Assignment1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        electricalOutlets(s);
    }

   

    public static void electricalOutlets(Scanner a) {
        int cases = a.nextInt();

        for (int i = 0; i < cases; i++) {
            int totaloutlets = 0;
            int outlets = a.nextInt();
            for (int j = 0; j < outlets; j++) {
                totaloutlets+= a.nextInt();
            }
            totaloutlets = totaloutlets - (outlets-1);
            System.out.println(totaloutlets);
        }
    }
}
