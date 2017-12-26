package Chess.Board;

import Chess.Pieces.Piece;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public abstract class Tile {
    //Set it to final and protected so that sub classes cannot change the value once it has been set
    protected final int tileNumber;
    //create a map of tiles
    private static Map<Integer, EmptyTile> BLANK_TILES_LIST = createAllEmptyTiles();

    private static Map<Integer,EmptyTile> createAllEmptyTiles() {
        //create a blank hashmap
        final Map<Integer, EmptyTile> allEmptyTiles = new HashMap<>();
        //populate the hashmap with blank tiles
        for (int i = 0; i <BoardUtils.TILES; i++){
            allEmptyTiles.put(i,new EmptyTile(i));
        }
        return Collections.unmodifiableMap(allEmptyTiles);
    }
    //if the tile to be created isn't null, return a tile with the piece on it
    //if its null, return one of the blank tiles created in the hashmap
    public static Tile createTile(final int tileNumber, Piece p){
        if (p!=null)
            return new OccupiedTile(tileNumber,p);
        else
            return BLANK_TILES_LIST.get(tileNumber);
    }
    Tile(final int tileNumber){
        this.tileNumber = tileNumber;
    }

    public abstract boolean tileOccupied();
    public abstract Piece getPiece();


}
