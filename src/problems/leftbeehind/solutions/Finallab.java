import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Finallab {
    public static void main(String[] args) {
       Scanner a = new Scanner(System.in);
       int b[] = new int[2];
        for (int i = 0; i < 2; i++) {
            b[i]= a.nextInt();
            
        }
        while(b[0]+(b[1]*b[1])!=0){
            if(b[0] + b[1]==13){
                System.out.println("Never speak again.");
            }
            else if(b[0]>b[1]){
               System.out.println("To the convention.");
           }else if(b[0]<b[1]){
               System.out.println("Left beehind.");
           }else if(b[0]==b[1]){
               System.out.println("Undecided.");
           }
           b[0] = a.nextInt();
           b[1] = a.nextInt();
        }
    }
    
}
