import java.util.ArrayList;
import java.util.Scanner;

public class Assignment1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        //echo(s);
        //greetings(s);
        reverse(s);
    }

    public static void echo(Scanner a) {
        String echo = a.next();
        for (int i = 0; i < 3; i++) {
            System.out.print(echo + " ");
        }
    }

    public static void greetings(Scanner a) {
        String greeting = a.next();
        int count = 0;
        ArrayList<Character> hey = new ArrayList<>();
        for (int i = 0; i < greeting.length(); i++) {
            hey.add(greeting.charAt(i));
            if (greeting.charAt(i) == 'e') {
                count++;
            }
        }

        for (int i = 0; i < count; i++) {
            hey.add(count + 1, 'e');
        }
        String result = new String();
        for (char c : hey) {
            result += c;
        }
        System.out.println(result);
    }

    public static void reverse(Scanner a) {
        int size = a.nextInt();
        int list[] = new int[size];
        for (int i = 0; i < size; i++) {
            list[i] = a.nextInt();
        }
        int newlist[] = new int[size];
        int count = size;
        for (int i = 0; i < list.length; i++) {
            newlist[i] = list[size - 1];
            size--;
        }
        for(int i : newlist){
            System.out.println(i);
        }
    }
}