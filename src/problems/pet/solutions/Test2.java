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
        
     
        int n = 4;
        
      int a = s.tokens().limit(n)  
            .mapToInt(f -> Integer.parseInt(f))  
              .sum();
       int b = s.tokens().limit(n)   
            .mapToInt(f -> Integer.parseInt(f))  
              .sum();
       int c = s.tokens().limit(n)   
            .mapToInt(f -> Integer.parseInt(f))  
              .sum();
        int d = s.tokens().limit(n)   
            .mapToInt(f -> Integer.parseInt(f))  
              .sum();
        int e = s.tokens().limit(n)   
            .mapToInt(f -> Integer.parseInt(f))  
              .sum();
        int[] nums = {a,b,c,d,e};
        int max = nums[0];
        int winner = 1;
        for (int i = 0; i < 5; i++) {
            if(nums[i]>max){
                max = nums[i];
                winner = i+1;
            }
            
        }
        System.out.print(winner+" ");
        System.out.println(max);
    }

}
