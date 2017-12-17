package Chess.Board;

import Chess.Pieces.Piece;

//abstract class for an empty tile
public final class EmptyTile extends Tile{
    EmptyTile(final int coord){
        super (coord);
    }
    //returns false because empty tiles will always be empty, and will therefore never have a piece
    @Override
    public boolean tileOccupied(){
        return false;
    }

    @Override
    public Piece getPiece(){
        return null;
    }
    @Override
    public String toString(){
        return "-";
    }
}