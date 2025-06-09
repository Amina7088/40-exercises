import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Result {

    /*
     * Complete the 'steadyGene' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING gene as parameter.
     */

public static int steadyGene(String gene) {
    int n = gene.length();
    int required = n / 4;
    Map<Character, Integer> count = new HashMap<>();
    
    for (char c : gene.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) + 1);
    }
    
    int minLength = n;
    int left = 0;
    
    for (int right = 0; right < n; right++) {
        count.put(gene.charAt(right), count.get(gene.charAt(right)) - 1);
        
        while (left < n && isSteady(count, required)) {
            minLength = Math.min(minLength, right - left + 1);
            count.put(gene.charAt(left), count.get(gene.charAt(left)) + 1);
            left++;
        }
    }
    return minLength;
}

private static boolean isSteady(Map<Character, Integer> count, int required) {
    return count.getOrDefault('A', 0) <= required &&
           count.getOrDefault('C', 0) <= required &&
           count.getOrDefault('G', 0) <= required &&
           count.getOrDefault('T', 0) <= required;
}

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String gene = bufferedReader.readLine();

        int result = Result.steadyGene(gene);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
