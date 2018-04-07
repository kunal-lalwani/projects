import java.util.Arrays;

/**
 * Created by kunal.lalwani on 05-Nov-17.
 */
public class HCalgorithm {

    public int[] firstChoiceHillClimbing(int n, int maxNumOfIterations) {
        int[] r = UtiliesSolving.generateRandomState(n);
        int costToBeat = UtiliesSolving.getHeuristicCost(r);

        for (int x = 0; x < maxNumOfIterations && costToBeat > 0; x++) {

            boolean flag = true;
            int tempCostToBeat = costToBeat;
            for (int col = 0; col < n && flag; col++) {

                for (int row = 0; row < n; row++) {
                    if (row == r[col])
                        continue;

                    // init new copy
                    int[] rc = Arrays.copyOf(r, n);
                    rc[col] = row;
                    int cost = UtiliesSolving.getHeuristicCost(rc);
                    if (costToBeat > cost) {
                        r[col] = row;
                        costToBeat = cost;
                        flag = false;
                        break;
                    }
                }
            }

            if (tempCostToBeat == costToBeat)
                r = UtiliesSolving.generateRandomState(n);

        }

        return costToBeat == 0 ? r : null; 
    }


    public int[] solve(int n, int maxNumOfIterations) {

        return firstChoiceHillClimbing(n, maxNumOfIterations);
    }

}
