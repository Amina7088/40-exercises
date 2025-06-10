import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collectors;

class Result {

    public static List<List<Integer>> knightlOnAChessboard(int n) {
        List<List<Integer>> result = new ArrayList<>();

        for (int a = 1; a < n; a++) {
            List<Integer> row = new ArrayList<>();
            for (int b = 1; b < n; b++) {
                int steps = bfs(n, a, b);
                row.add(steps);
            }
            result.add(row);
        }

        return result;
    }

    private static int bfs(int n, int a, int b) {
        int[][] directions = {
            {a, b}, {a, -b}, {-a, b}, {-a, -b},
            {b, a}, {b, -a}, {-b, a}, {-b, -a}
        };

        boolean[][] visited = new boolean[n][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 0});  // row, col, steps
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], steps = curr[2];

            if (r == n - 1 && c == n - 1) {
                return steps;
            }

            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    queue.offer(new int[]{nr, nc, steps + 1});
                }
            }
        }

        return -1;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> result = Result.knightlOnAChessboard(n);

        for (List<Integer> row : result) {
            String line = row.stream()
                .map(Object::toString)
                .collect(Collectors.joining(" "));
            bufferedWriter.write(line);
            bufferedWriter.newLine();
        }

        bufferedReader.close();
        bufferedWriter.flush();
        bufferedWriter.close();
    }
}
