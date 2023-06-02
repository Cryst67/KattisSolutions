import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Finallab {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int limit = a.nextInt();
        String red = "simon says ";
        for (int i = 0; i < limit+1; i++) {
            String b = a.nextLine();
            
            if(b.contains(red)){
                 b = b.replace(red, "");
                
            }else{
                b = "";
                
            }
            System.out.println(b);
            
        }
        
    }
    
}
