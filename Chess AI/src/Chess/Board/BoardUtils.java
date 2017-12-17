package Chess.Board;

public class BoardUtils {
    public static final boolean [] COL_ONE = createCol(0);
    public static final boolean [] COL_TWO = createCol(2);
    public static final boolean [] COL_THREE = null;
    public static final boolean [] COL_FOUR = null;
    public static final boolean [] COL_FIVE = null;
    public static final boolean [] COL_SIX = null;
    public static final boolean [] COL_SEVEN = createCol(6);
    public static final boolean [] COL_EIGHT = createCol(7);

    public static final boolean [] ROW_TWO = createRows(8);
    public static final boolean [] ROW_SEVEN = createRows(48);

    //set final constants for number of tiles on a board, and row/col tiles
    public static final int TILES = 64;
    public static final int RCTILES = 8;
    //populate the needed array with 'true' in the given column
    private static boolean[] createCol(int i) {
        boolean [] column = new boolean[TILES];
        for (;i<TILES;i+=RCTILES)
            column[i] = true;
        return column;
    }
    private static boolean [] createRows(int i){
        boolean [] row = new boolean[TILES];
        for (;i%TILES!=0;i++)
            row[i] = true;
        return row;
    }
    private BoardUtils(){
        System.out.println("Cannot create a board utils class");
    }
    //if position out of bounds, return false, if its within bounds return true
    public static boolean legalTile(int coord) {
        return coord >=0 && coord <64;
    }
}
