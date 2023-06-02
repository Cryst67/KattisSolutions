import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;

public class Assignment {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        //System.out.println(keywords(a.nextInt(), a));
        //oddmanout(a);
        securedoors(a);
    }

    public static long keywords(int limit, Scanner a) {

        a.nextLine();
        int count = 0;
        Set<String> b = new HashSet<>();
        while (count < limit) {

            String temp = a.nextLine();
            String temp2 = temp.replaceAll("-", " ");

            String last = temp2.toLowerCase();

            b.add(last);
            count++;
        }
        return b.stream().count();
    }
    
    public static void oddmanout(Scanner a){
        int limit = a.nextInt();
        int count = 0;
        while(count < limit){
             HashSet<Integer> b = new HashSet<>();
             int guests = a.nextInt();
             int c;
             for (int i = 0; i < guests; i++) {
                c = a.nextInt();
                if(b.contains(c)){
                    b.remove(c);
                }else{
                    b.add(c);
                }
            }
             System.out.println("Case #"+(count+1)+": "+(b.toArray())[0]); 
    }
        
}
    public static void securedoors(Scanner a){
        int limit = a.nextInt();
        a.nextLine();
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < limit; i++) {
            String temp = a.nextLine();
            String b[] = temp.split(" ");
            if(b[0].equals("entry") && set.contains(b[1])){
                System.out.println(b[1]+ " entered (ANOMALY)");
            }else if(b[0].equals("exit") && !set.contains((b[1]))){
                System.out.println((b[1]+ " exited (ANOMALY)"));
            }else if(b[0].equals("entry")){
                set.add(b[1]);
                System.out.println(b[1]+ " entered");
            }else{
                set.remove(b[1]);
                System.out.println(b[1]+ " exited");
            }
        }
    }
}