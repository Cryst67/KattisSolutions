import java.util.Scanner;

public class racingalphabet {
  final static double dist = 60f * Math.PI;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int cases = Integer.parseInt(sc.nextLine());
    for (int i = 0; i < cases; i++) {
      String line = sc.nextLine();
      int linelen = line.length()-1;
      int dist = 0;
      for (int j = 0; j < linelen; j++) {
        int src = line.charAt(j) == ' ' ? 27 : line.charAt(j) == '\'' ? 28 : line.charAt(j) - 64;
        int dest = line.charAt(j+1) == ' ' ? 27 : line.charAt(j+1) == '\'' ? 28 : line.charAt(j+1) - 64;
        int diff = src - dest < 0 ? dest - src : src - dest;
        dist += diff > 14 ? 28 - diff : diff;
      }
      System.out.println(dist * racingalphabet.dist / 420f + line.length());
    }
  }
}