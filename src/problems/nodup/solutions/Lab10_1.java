package lab10;

import java.util.*;

public class Lab10 {

    public static void main(String[] args) {

       
        nodup();
    }

  
    public static void nodup() {
        Scanner a = new Scanner(System.in);
        ArrayList<String> b = new ArrayList<>();

        while (a.hasNext()) {
            String c = a.next();
            
            if (c.equals("a")) {
                break;
            }
            b.add(c);
        }
        if(check(b)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
        
            

        }
    
    public static boolean check(ArrayList<String> a){
        for (int i = 0; i < a.size(); i++) {
            String c = a.get(i);
            int j;
            for (j = i + 1; j < a.size(); j++) {
                if (c.equals(a.get(j))) {
                    return false;
                    
                }

            }
        
    }
        return true;
    }
}

