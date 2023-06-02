import java.util.*;
public class Costumecontest {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int limit = a.nextInt();
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < limit; i++) {
            
            String costume = a.next();
            int count = map.getOrDefault(costume, 0)+1;
            map.put(costume, count);
            
        }
        int min = limit +1;
        Set<String> costumes = map.keySet();
        for(String costume :costumes){
            min = Math.min(min, map.get(costume));
            
        }
        
        List<String> winner = new ArrayList<>();
        for(String costume : costumes){
            if(map.get(costume) == min){
                winner.add(costume);
            }
        }
        winner.stream().sorted().forEach(System.out::println);
    }
    
}
