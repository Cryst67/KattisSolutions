import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt(),b = s.nextInt();
        int[] list = {a,b};
        if(a<b){
            list[0]= a;
            list[1]=b;
        }else{
            list[0]=b;
            list[1]=a;
        }
        
        for (int i = 0; i < list.length; i++) {
            System.out.print(list[i]+ " ");
        }
        
        
    }

}
