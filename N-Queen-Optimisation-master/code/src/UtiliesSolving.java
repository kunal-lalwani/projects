import javafx.collections.transformation.SortedList;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
/**
 * Created by Kunal Lalwani on 07-Nov-17.
 */
public class UtiliesSolving {

    public static int[] allState(int n) {

        return new int[n];
    }

    public static int[] randomState(int[] r) {

        for (int i = 0; i < r.length; i++)
            r[i] = (int) (Math.random() * r.length);

        return r;
    }

    public static int[] generateRandomState(int n) {

        return randomState(allState(n));
    }

    public static int getHeuristicCost(int[] r) {
        int h = 0;

        for (int i = 0; i < r.length; i++)
            for (int j = i + 1; j < r.length; j++)
                if (r[i] == r[j] || Math.abs(r[i] - r[j]) == j - i)
                    h += 1;

        return h;
    }



}
