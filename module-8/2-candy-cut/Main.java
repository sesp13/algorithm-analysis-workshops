import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void getMinMaxCosts(int arrLength, int[] p) {
        int[][] r = new int[arrLength][arrLength];
        // Init values
        r[0][0] = p[0];
        r[0][1] = p[0];
        for (var i = 1; i < arrLength; i++) {
            // Init values
            r[i][0] = p[i];
            r[i][1] = p[i];
            for (var j = 0; j < i; j++) {
                int pj = p[j];
                int restIndex = i - j - 1;
                // Fill for the min proccess
                r[i][0] = Math.min(r[i][0], pj + r[restIndex][0]);
                // Fill for the max procceses
                r[i][1] = Math.max(r[i][1], pj + r[restIndex][1]);
            }
        }
        int lastIndex = arrLength - 1;
        System.out.println(r[lastIndex][0] + " " + r[lastIndex][1]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int cases = Integer.parseInt(st.nextToken());
        for (int i = 0; i < cases; i++) {
            st = new StringTokenizer(br.readLine());
            int n = st.countTokens();
            int arrLength = Integer.parseInt(st.nextToken());
            int[] p = new int[n - 1];
            for (int j = 0; j < n - 1; j++) {
                p[j] = Integer.parseInt(st.nextToken());
            }
            getMinMaxCosts(arrLength, p);
        }

    }
}