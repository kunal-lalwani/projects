import javafx.collections.ObservableList;
import javafx.collections.transformation.SortedList;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Created by kunal.lalwani on 15-Nov-17.
 */
public class LBSalgorithm {


    public int[] solve(int n, int maxNumOfIterations, int numOfStates) {
        int[][] states = new int[numOfStates][];

        for (int i = 0; i < numOfStates; i++)
            states[i] = UtiliesSolving.generateRandomState(n);


        for (int x = 0; x < maxNumOfIterations; x++) {

            int[][] newStates = new int[n*numOfStates][];
            for (int i = 0; i < numOfStates; i++) {
                int costToBeat = UtiliesSolving.getHeuristicCost(states[i]);

                if (costToBeat == 0)
                    return states[i];

                for (int col = 0; col < n; col++) {
                    newStates[i*n + col] = makeMove(states[i], col, costToBeat);

                    if (newStates[i*n + col] == null)
                        newStates[i*n + col] = UtiliesSolving.generateRandomState(n);
                }

            }
            Arrays.sort(newStates, Comparator.comparingInt(UtiliesSolving::getHeuristicCost));

            states = Arrays.copyOfRange(newStates, 0, numOfStates);

        }

        return null;
    }

    private int[] makeMove(int r[], int col, int costToBeat) {
        int n = r.length;

        for (int row = 0; row < n; row++) {
            if (row == r[col])
                continue;

            int tmpRow = r[col];
            r[col] = row;
            int cost = UtiliesSolving.getHeuristicCost(r);
            if (costToBeat > cost) {
                r[col] = row;
                return r;
            }
            r[col] = tmpRow;
        }

        return null;
    }


}
