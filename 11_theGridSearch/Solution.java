import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'gridSearch' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING_ARRAY G
     *  2. STRING_ARRAY P
     */

public static String gridSearch(String[] G, String[] P) {
    int Row = G.length;  
    int Col = G[0].length(); 
    int row = P.length;      
    int col = P[0].length();  

    for (int i = 0; i <= Row- row; i++) {
        for (int j = 0; j <= Col - col; j++) {
            boolean match = true;

            for (int x = 0; x < row; x++) {
                String subG = G[i + x].substring(j, j + col); 

                if (!subG.equals(P[x])) {
                    match = false;  
                    break;
                }
            }

            if (match) {
                return "YES";
            }
        }
    }

    return "NO"; 
}


}

public class Solution {
   public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

    int t = Integer.parseInt(bufferedReader.readLine().trim());

    IntStream.range(0, t).forEach(tItr -> {
        try {
            String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            int R = Integer.parseInt(firstMultipleInput[0]);
            int C = Integer.parseInt(firstMultipleInput[1]);

            List<String> G = IntStream.range(0, R).mapToObj(i -> {
                try {
                    return bufferedReader.readLine();
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            }).collect(toList());

            String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            int r = Integer.parseInt(secondMultipleInput[0]);
            int c = Integer.parseInt(secondMultipleInput[1]);

            List<String> P = IntStream.range(0, r).mapToObj(i -> {
                try {
                    return bufferedReader.readLine();
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            }).collect(toList());

            String[] gArr = G.toArray(new String[0]);
            String[] pArr = P.toArray(new String[0]);

            String result = Result.gridSearch(gArr, pArr);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    });

    bufferedReader.close();
    bufferedWriter.close();
}

}
