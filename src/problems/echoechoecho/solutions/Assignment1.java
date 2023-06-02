import java.util.Scanner;
public class Assignment1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        echo(s);
    }
    
    public static void echo(Scanner a){
        String echo = a.next();
        for (int i = 0; i < 3; i++) {
            System.out.print(echo+" ");
        }
    }
}
