import java.io.*;

class Result {

    /*
     * Complete the 'encryption' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

        public static String encryption(String s) {
            s = s.replaceAll("\\s", ""); 
            int length = s.length();

            double sqrt = Math.sqrt(length);
            int row = (int) Math.floor(sqrt);
            int column = (int) Math.ceil(sqrt);
            if (row * column < length) {
                row++;
            }

            String encrypt = "";

            for (int c = 0; c < column; c++) {
                for (int r = 0; r < row; r++) {
                    int index = r * column + c;
                    if (index < length) {
                        encrypt += s.charAt(index);
                    }
                }
                encrypt += " ";
            }

            return encrypt.trim();
        }



}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
