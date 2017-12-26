package Chess.Board;


import Chess.Pieces.Piece;

//
public final class OccupiedTile extends Tile{
    //the Piece that will be on this tile
    private final Piece p;
    OccupiedTile(final int coord, Piece p){
        super(coord);
        this.p = p;
    }

    @Override
    public boolean tileOccupied(){
        return true;
    }
    @Override
    public Piece getPiece(){
        return p;
    }
    @Override
    public String toString(){
        return getPiece().getPieceColor().isBlack() ? getPiece().toString().toLowerCase() : getPiece().toString();
    }
}