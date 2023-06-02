package lab10;

import java.util.*;

public class Lab10 {

    public static void main(String[] args) {

        //integer();
        //string();
        //integersum();
        nodup();
    }

    public static void integer() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);

        list.set(1, 99);
        int y = list.get(1);
        int size = list.size();
        System.out.println(list);
        System.out.println(list.contains(3));
        Collections.sort(list);
        System.out.println(list);

    }

    public static void string() {
        ArrayList<String> list = new ArrayList<>();
        list.add("Zach");
        list.add("Alice");
        list.add("Bob");
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);
        list.remove(0);
        System.out.println(list);
        list.remove("Zach");
        System.out.println(list);
    }

    public static void integersum() {
        Scanner a = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        int count = 0;
        while (count < 10) {
            list.add(a.nextInt());
            count++;
        }
        int sum = 0;
        for (int i = 0; i < list.size(); i++) {
            sum += list.get(i);
        }
        System.out.println(sum);
        sum = 0;
        list.remove(list.size() - 1);
        for (int b : list) {
            sum += b;
        }
        System.out.println(sum);
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

