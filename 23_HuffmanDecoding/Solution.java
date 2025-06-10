import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;

class Node implements Comparable<Node> {
    int freq;
    char data;
    Node left, right;

    public Node(int freq, char data) {
        this.freq = freq;
        this.data = data;
    }

    public Node(int freq, char data, Node left, Node right) {
        this.freq = freq;
        this.data = data;
        this.left = left;
        this.right = right;
    }

    public int compareTo(Node other) {
        return this.freq - other.freq;
    }

    public boolean isLeaf() {
        return left == null && right == null;
    }
}

public class Solution {
    static Map<Character, String> codeMap = new HashMap<>();

    static void buildCodes(Node root, String code) {
        if (root == null) return;
        if (root.isLeaf()) {
            codeMap.put(root.data, code.length() > 0 ? code : "0");
        }
        buildCodes(root.left, code + "0");
        buildCodes(root.right, code + "1");
    }

    static Node buildTree(Map<Character, Integer> freqMap) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            pq.add(new Node(entry.getValue(), entry.getKey()));
        }

        while (pq.size() > 1) {
            Node a = pq.poll();
            Node b = pq.poll();
            Node merged = new Node(a.freq + b.freq, '\0', a, b);
            pq.add(merged);
        }

        return pq.poll();
    }

    static void decode(Node root, String s) {
        Node current = root;
        for (char c : s.toCharArray()) {
            current = (c == '0') ? current.left : current.right;
            if (current.isLeaf()) {
                System.out.print(current.data);
                current = root;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        Map<Character, Integer> freq = new HashMap<>();
        for (char c : input.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        Node root = buildTree(freq);
        buildCodes(root, "");

        StringBuilder encoded = new StringBuilder();
        for (char c : input.toCharArray()) {
            encoded.append(codeMap.get(c));
        }

        decode(root, encoded.toString());
    }
}
