import java.util.*;

public class Kattis {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int cases = Integer.parseInt(sc.nextLine());
    for (int k = 0; k < cases; k++) {
      String[] line = sc.nextLine().split("([ /])");

      int num = Integer.parseInt(line[0]);
      int numerator = Integer.parseInt(line[1]);
      int denominator = Integer.parseInt(line[2]);

      StringBuilder sb = new StringBuilder();
      while(numerator > 1 || denominator > 1){
        if(denominator > numerator) {
          denominator -= numerator;
          sb.append('L');
        }
        else{
          numerator -= denominator;
          sb.append('R');
        }
      }
      char [] arr = sb.reverse().toString().toCharArray();
      int i = 1;
      for (char anArr : arr) {
        i *= 2;
        if (anArr == 'R') {
          i++;
        }
      }
      System.out.println(num + " " + i);
    }
  }
}