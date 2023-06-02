import java.util.*;

/**
 *
 * @author suviksh
 */
public class Recount {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        TreeMap<String, Integer> map = new TreeMap();
        while (true) {
            String name = a.nextLine();
            if (name.equals("***")) {
                break;
            }
            int count = map.getOrDefault(name, 0) + 1;
            map.put(name, count);
        }
        int max = 0;
        Set<String> candidates = map.keySet();
        for(String cand: candidates){
            max = Math.max(max, map.get(cand));
            
        }
        List<String> winners = new ArrayList<>();
        for(String cand : candidates){
            if(map.get(cand) == max){
                winners.add(cand);
            }
        }
        if(winners.size()>1){
            System.out.println("Runoff!");
        }else{
            System.out.println(winners.toArray()[0]);
        }
    }

}