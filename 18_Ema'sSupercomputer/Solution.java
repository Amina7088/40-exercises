import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import static java.util.stream.Collectors.toList;
import java.util.stream.IntStream;

class Result {

    /*
     * Complete the 'twoPluses' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING_ARRAY grid as parameter.
     */
    public static int twoPluses(List<String> grid) {
        int n = grid.size();
        int m = grid.get(0).length();
        List<Plus> pluses = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int size = 0;
                while (canMakePlus(grid, i, j, size)) {
                    pluses.add(new Plus(i, j, size));
                    size++;
                }
            }
        }

        int maxProduct = 0;
        for (int i = 0; i < pluses.size(); i++) {
            for (int j = i + 1; j < pluses.size(); j++) {
                Plus p1 = pluses.get(i);
                Plus p2 = pluses.get(j);
                if (!p1.overlaps(p2)) {
                    int product = p1.area() * p2.area();
                    maxProduct = Math.max(maxProduct, product);
                }
            }
        }

        return maxProduct;
    }

    static class Plus {
        int row, col, size;
        Set<String> cells;

        Plus(int row, int col, int size) {
            this.row = row;
            this.col = col;
            this.size = size;
            this.cells = new HashSet<>();
            cells.add(row + "," + col);
            for (int k = 1; k <= size; k++) {
                cells.add((row + k) + "," + col);
                cells.add((row - k) + "," + col);
                cells.add(row + "," + (col + k)); 
                cells.add(row + "," + (col - k)); 
            }
        }

        int area() {
            return 4 * size + 1;
        }

        boolean overlaps(Plus other) {
            for (String cell : this.cells) {
                if (other.cells.contains(cell)) {
                    return true;
                }
            }
            return false;
        }
    }

    static boolean canMakePlus(List<String> grid, int row, int col, int size) {
        int n = grid.size();
        int m = grid.get(0).length();

        try {
            if (grid.get(row).charAt(col) != 'G') return false;
            for (int k = 1; k <= size; k++) {
                if (grid.get(row + k).charAt(col) != 'G') return false;
                if (grid.get(row - k).charAt(col) != 'G') return false;
                if (grid.get(row).charAt(col + k) != 'G') return false;
                if (grid.get(row).charAt(col - k) != 'G') return false;
            }
        } catch (IndexOutOfBoundsException e) {
            return false;
        }

        return true;
    }
}



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<String> grid = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        int result = Result.twoPluses(grid);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
