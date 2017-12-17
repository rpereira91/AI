package Chess.Pieces;

import Chess.Board.*;
import Chess.PieceColor;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class King extends  Piece {

    private static int [] POSSIBLE_MOVES = {1,7,8,9,-1,-7,-8,-9};
    public King(int position, PieceColor pieceColor) {
        super(position, pieceColor,PieceType.KING);
    }

    @Override
    public Collection<Move> allLegalMoves(Board board) {
        int destPosition;
        List<Move> possibleMoves = new ArrayList<>();
        for (int po: POSSIBLE_MOVES){
            destPosition = this.position + po;
            if (inFirstCol(this.position,po) || inEighthCol(this.position,po))
                continue;
            if(BoardUtils.legalTile(destPosition)){
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
    @Override
    public String toString(){
        return PieceType.KING.toString();
    }
    private static boolean inFirstCol(int current, int offset) {
        return BoardUtils.COL_ONE[current] && ((offset == -9) || (offset == -1) || (offset == 7));
    }

    private static boolean inEighthCol(int current, int offset) {
        return BoardUtils.COL_EIGHT[current] && ((offset == -7) || (offset == 1) || (offset == 9));
    }
}
