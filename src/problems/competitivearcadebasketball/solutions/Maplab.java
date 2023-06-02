import java.util.*;
public class Maplab {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);    
        int players = a.nextInt();
        int minpoint = a.nextInt();
        int lines = a.nextInt();
        TreeMap<String,Integer> map = new TreeMap<>();
        for (int i = 0; i < players; i++) {
            String c = a.next();
            
            map.put(c,0);
        }
        Set<String> winners = new LinkedHashSet<>();
        for (int i = 0; i < lines; i++) {
            String player = a.next();
            int score = a.nextInt();
            int count = map.get(player);
           map.put(player, count + score);
           if(map.get(player)>= minpoint){
               winners.add(player);
           }
        }
        
        
        
        
        if(winners.size() > 0){
        winners.stream().map(d-> d + " wins!").forEach(System.out::println);
        }else {
            System.out.println("No winner!");
        }
    }
    
    
}
