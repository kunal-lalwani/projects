
public class BackTrack {
	static int N = 8;
    static  int k = 1;
	public static void main(String[] args) {
		solution();
	}
	
	public static void solution()
	{
	    int board[][] = new int[N][N];
	    if (solve(board, 0))
	    {
	        System.out.println("Solution does not exist");
	        return ;
	    }
	}
	
	public static boolean solve(int chessboard[][], int col)
	{
	    if (col == N )
	    {
	        printSolution(chessboard);
	        return true;
	    }
	 
	    for (int i = 0; i < N; i++)
	    {
	        if ( isSafe(chessboard, i, col) )
	        {
	            chessboard[i][col] = 1;
	            solve(chessboard, col + 1) ;
	            chessboard[i][col] = 0; 
	        }
	    }
	 
	    return false;
	}
	public static boolean isSafe(int chessboard[][], int row, int col)
	{
	    int i, j;
	 
	    for (i = 0; i < col; i++)
	        if (chessboard[row][i]==1)
	            return false;
	 
	    for (i=row, j=col; i>=0 && j>=0; i--, j--)
	        if (chessboard[i][j]==1)
	            return false;
	 
	    for (i=row, j=col; j>=0 && i<N; i++, j--)
	        if (chessboard[i][j]==1)
	            return false;
	 
	    return true;
	}
	public static void printSolution(int chessboard[][])
	{
	    System.out.println(k++);
	    for (int i = 0; i < N; i++)
	    {
	        for (int j = 0; j < N; j++)
	            System.out.print(chessboard[i][j]);
	        System.out.println();
	    }
	    System.out.println();
	}
}
