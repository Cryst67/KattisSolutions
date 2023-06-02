
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Finallab {
    public static void main(String[] args) {
       Scanner a = new Scanner(System.in);
       int b  = a.nextInt();
       int c = a.nextInt();
       int d = a.nextInt();
        for (int i = 0; i < d; i++) {
            int e = i+1;
            if(e %(b)==0 && e%c ==0){
                System.out.println("FizzBuzz");
            }else if(e%b == 0){
                System.out.println("Fizz");
            }else if(e%c == 0){
                System.out.println("Buzz");
            }else{
                System.out.println(e);
            }
            
        }
    }
    
}
