import java.net.URL;

import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.geometry.Insets;
import javafx.scene.control.Label;
import javafx.scene.control.SplitPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.CornerRadii;
import javafx.scene.paint.Color;

/**
 * Created by Kunal Lalwani on 07-Nov-17.
 */
public class SessionController {

	long startTime, endTime, duration[][] = new long[4][];
	int HCCounter=0, SACounter = 0, LBSCounter = 0, GACounter = 0;
    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private BorderPane mainWordPane;

    @FXML
    private Label noSolutionLabel;

    @FXML
    private TextField saTemperature;

    @FXML
    private TextField saCoolingFactor;

    @FXML
    private TextField lbIterations;

    @FXML
    private TextField hcIterations;

    @FXML
    private TextField queens;

    @FXML
    private SplitPane splitWordList;

    @FXML
    private TextField saIterations;

    @FXML
    private TextField lbStates;

    @FXML
    private TextField gaGenerations;

    @FXML
    private TextField gaInitialPopulationSize;

    @FXML
    private TextField gaMutationProbability;

    FrontEnd guiPuzzle = new FrontEnd();

    private int getNum(TextField tf) {
        return Integer.parseInt(tf.getText());
    }
    private double getDouble(TextField tf) {
        return Double.parseDouble(tf.getText());
    }

    @FXML
    void runHillClimbing(ActionEvent event) {
    	startTime = System.nanoTime();
        HCalgorithm hCalgorithm = new HCalgorithm();
        int[] res = hCalgorithm.solve(getNum(queens), getNum(hcIterations));
        endTime = System.nanoTime();
        System.out.println("The duration is");
        System.out.println(endTime - startTime);
        duration[1][HCCounter++] = endTime - startTime;
        showResult(res);
    }

    @FXML
    void runSimulatedAnnealing(ActionEvent event) {
    	startTime = System.nanoTime();
        SAalgorithm sAalgorithm = new SAalgorithm();

        int[] res = sAalgorithm.solve(getNum(queens), getNum(saIterations), getDouble(saTemperature), getDouble(saCoolingFactor));

        endTime = System.nanoTime();
        System.out.println("The duration is");
        System.out.println(endTime - startTime);
        
        showResult(res);
    }

    private void showResult(int[] res) {
        guiPuzzle.drawQueens(res);
        noSolutionLabel.setVisible(res == null);
    }

    @FXML
    void runLocalBeamSearch(ActionEvent event) {
    	startTime = System.nanoTime();

        LBSalgorithm lBSalgorithm = new LBSalgorithm();

        int[] res = lBSalgorithm.solve(getNum(queens), getNum(lbIterations), getNum( lbStates));
        
        endTime = System.nanoTime();
        System.out.println("The duration is");
        System.out.println(endTime - startTime);
        showResult(res);
    }

    @FXML
    void runGeneticAlgorithm(ActionEvent event) {
    	startTime = System.nanoTime();

        GeneticAlgorithm geneticAlgorithm = new GeneticAlgorithm();
        int[] res = geneticAlgorithm.solve(getNum(queens), getNum(gaInitialPopulationSize), getDouble(gaMutationProbability), getNum(gaGenerations));

        endTime = System.nanoTime();
        System.out.println("The duration is");
        System.out.println(endTime - startTime);
        showResult(res);
    }

    @FXML
    void initialize() {
        

        mainWordPane.setCenter(guiPuzzle);
        mainWordPane.setBackground(new Background(new BackgroundFill(Color.ANTIQUEWHITE, CornerRadii.EMPTY, new Insets(0, 0, 0, 0))));

    }
}
