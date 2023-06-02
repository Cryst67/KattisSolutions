import java.util.*;

public class Main {
public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    int[] a = {s.nextInt(),s.nextInt(),s.nextInt()};
    
    Arrays.sort(a);
    
    ArrayList<Character> c= new ArrayList<>();
    String d = s.next();
    c.add(d.charAt(0));
    c.add(d.charAt(1));
    c.add(d.charAt(2));
    
    for(char f : c){
        if(f == 'A'){
            System.out.print(a[0]+" ");
        }else if(f =='B'){
            System.out.print(a[1]+ " ");
            
        }else if(f == 'C'){
            System.out.println(a[2]+" ");
        }
            
    }
}

}