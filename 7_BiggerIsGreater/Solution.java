import java.io.*;

class Result {

    /*
     * Complete the 'biggerIsGreater' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING w as parameter.
     */

    public static String biggerIsGreater(String w) {
        char[] chars = w.toCharArray();
        int i = chars.length-2;
        
        while (i >= 0 && chars[i] >= chars[i + 1]) {
                    i--;
                }    
        if (i==-1){
            return "no answer";
        }
        int j = chars.length - 1;
        while (chars[j] <= chars[i]) {
            j--;
        }
        
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;

        reverse(chars, i + 1, chars.length - 1);

        return new String(chars);
    }
    private static void reverse(char[] arr, int start, int end) {
        while (start < end) {
            char a = arr[start];
            arr[start] = arr[end];
            arr[end] = a;
            start++;
            end--;
        }
    }
 }



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int T = Integer.parseInt(bufferedReader.readLine().trim());

        for (int TItr = 0; TItr < T; TItr++) {
            String w = bufferedReader.readLine();

            String result = Result.biggerIsGreater(w);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedReader.close();
        bufferedWriter.close();
    }
}
