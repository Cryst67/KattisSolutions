
import java.math.BigInteger;
import java.util.Scanner;

public class Finallab {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        BigInteger c = new BigInteger("0");
        c = a.nextBigInteger();
        String b = a.next();
        if(b.equals("*")){
            c = c.multiply(new BigInteger(a.next()));
        }
        if(b.equals("+")){
            c = c.add(new BigInteger(a.next()));
        }
        System.out.println(c);
    }
    
}
