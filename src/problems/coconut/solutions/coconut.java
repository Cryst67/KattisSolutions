import java.io.*;
import java.util.*;
//Code by wentinggy
//Couldn't be bothered reading the problem
class Player {
    public int playerNum;
    public String actionState;

    // "a" : hands still folded
    // "b" : two fists
    // "c" : hand turned palm down
    // "d" : behind the back
    public Player(int playerNum, String actionState) {
        this.playerNum = playerNum;
        this.actionState = actionState;
    }
    boolean isFolded() {
        return (this.actionState == "a") ? true : false;
    }
    
    boolean isTwoFists() {
        return (this.actionState == "b") ? true : false;
    }
    
    boolean isPalmDown() {
        return (this.actionState == "c") ? true : false;
    }
}

public class coconut {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

        // first line of input
        int totalSyllabus = io.getInt();
        int numOfPlayers = io.getInt();

        ArrayList<Player> playerArr = new ArrayList<Player>();
        for (int i = 1; i< numOfPlayers + 1; i++) {  
            playerArr.add(new Player(i, "a"));
        }

        int playerId = 0;
        while (playerArr.size() > 1) {
            playerId =  (playerId + totalSyllabus -1) % playerArr.size();
            Player currentPlayer = playerArr.get(playerId);

            if (currentPlayer.isFolded()) {
                playerArr.set(playerId, new Player(currentPlayer.playerNum, "b"));
                playerArr.add(playerId, (new Player(currentPlayer.playerNum, "b")));

            } else if (currentPlayer.isTwoFists()) {
                playerArr.set(playerId, new Player(currentPlayer.playerNum, "c"));
                playerId++;

            } else if (currentPlayer.isPalmDown()) {
                playerArr.remove(playerId);
            }
        }
        io.println(playerArr.get(0).playerNum);
        io.close();
    }
}

class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
        super(new BufferedOutputStream(System.out));
        r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
        super(new BufferedOutputStream(o));
        r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
        return peekToken() != null;
    }

    public int getInt() {
        return Integer.parseInt(nextToken());
    }

    public double getDouble() {
        return Double.parseDouble(nextToken());
    }

    public long getLong() {
        return Long.parseLong(nextToken());
    }

    public String getWord() {
        return nextToken();
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
        if (token == null)
            try {
                while (st == null || !st.hasMoreTokens()) {
                    line = r.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                }
                token = st.nextToken();
            } catch (IOException e) { }
        return token;
    }

    private String nextToken() {
        String ans = peekToken();
        token = null;
        return ans;
    }
}