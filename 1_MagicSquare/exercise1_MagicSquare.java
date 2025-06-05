import java.util.*;

class Result {

    public static int formingMagicSquare(List<List<Integer>> s) {
        int[][][] MagicSquare = {
            {{8,1,6},{3,5,7},{4,9,2}},
            {{6,1,8},{7,5,3},{2,9,4}},
            {{4,9,2},{3,5,7},{8,1,6}},
            {{2,9,4},{7,5,3},{6,1,8}},
            {{8,3,4},{1,5,9},{6,7,2}},
            {{4,3,8},{9,5,1},{2,7,6}},
            {{6,7,2},{1,5,9},{8,3,4}},
            {{2,7,6},{9,5,1},{4,3,8}}
        };

        int minimalCost = Integer.MAX_VALUE;

        for (int i = 0; i < 8; i++) {
            int cost = 0;
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    cost += Math.abs(s.get(j).get(k) - MagicSquare[i][j][k]);
                }
            }
            minimalCost = Math.min(minimalCost, cost);
        }
        return minimalCost;
    }
}

public class exercise1_MagicSquare {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<List<Integer>> s = new ArrayList<>();

        System.out.println("3x3 matritsiin utga:");

        for (int i = 0; i < 3; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < 3; j++) {
                row.add(scanner.nextInt());
            }
            s.add(row);
        }

        int result = Result.formingMagicSquare(s);

        System.out.println("min cost:" + result);
        scanner.close();
    }
}
