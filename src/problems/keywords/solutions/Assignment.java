import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;

public class Assignment {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int limit = a.nextInt();
        a.nextLine();
        int count = 0;
        Set<String> b = new HashSet<>();
        while(count <limit){
            
            String temp = a.nextLine();
            String temp2 = temp.replaceAll("-", " ");
            
            String last = temp2.toLowerCase();
            
            b.add(last);
            count++;
        }
        System.out.println(b.stream().count());
    }
    
}
