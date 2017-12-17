package Chess.Pieces;

import Chess.Board.*;
import Chess.PieceColor;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Knight extends Piece{
    //an array of all possible moves that the knight can make on the board.
    //Not all these are possible however as we need to check if a piece is occupying any of these spots
    private static int[] POSSIBLE_MOVES = { -17, -15, -10, -6, 6, 10, 15, 17 };
    public Knight(final int position, final PieceColor pieceColor) {
        super(position, pieceColor,PieceType.KING);
    }
    //get all the legal moves for the knight
    @Override
    public Collection<Move> allLegalMoves(Board board) {
        int destPosition;
        List<Move> possibleMoves = new ArrayList<>();
        //for each element in the possible move list
        for(int po : POSSIBLE_MOVES){
            //the possible destnation is the offset in the possible moves plus the possible destnation
            destPosition = this.position + po;
            //if the spot is valid
            //I need to add some logic here
            if(BoardUtils.legalTile(destPosition)){
                if (inFirstCol(this.position,po) ||
                        inSecondCol(this.position,po)||
                        inSeventhCol(this.position,po)||
                        inEighthCol(this.position,po)){
                    continue;
                }
                Tile destTile = board.getTile(destPosition);
                //if the tile is free add it to the possible move list
                if(!destTile.tileOccupied()){
                    possibleMoves.add(new NonAttackMove(board,this,po));
                }
                //if the tile is not free check the color of the tile
                else{
                    Piece pieceInTheWay = destTile.getPiece();
                    PieceColor colorInTheWay = pieceInTheWay.getPieceColor();
                    //if the tile is an enemy tile add it to the move list
                    if(this.pieceColor !=  colorInTheWay){
                        possibleMoves.add(new AttackMove(board,this,po,pieceInTheWay));
                    }
                }
            }
        }
        return possibleMoves;
    }
    //if the knight is in specific columns they can't move legally to places based on the offset
    private static boolean inFirstCol(int current, int offset) {
        return BoardUtils.COL_ONE[current] && ((offset == -17) || (offset == -10) || (offset == 6) || (offset == 15));
    }

    private static boolean inSecondCol(int current, int offset) {
        return BoardUtils.COL_TWO[current] && ((offset == -10) || (offset == 6));
    }

    private static boolean inSeventhCol(int current, int offset) {
        return BoardUtils.COL_SEVEN[current] && ((offset == -6) || (offset == 10));

    }
    private static boolean inEighthCol(int current, int offset) {
        return BoardUtils.COL_EIGHT[current] && ((offset == -15) || (offset == -6) || (offset == 10) || (offset == 17));
    }
    @Override
    public String toString(){
        return PieceType.KNIGHT.toString();
    }
}

