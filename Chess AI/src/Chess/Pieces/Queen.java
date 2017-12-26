package Chess.Pieces;

import Chess.Board.*;
import Chess.PieceColor;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Queen extends  Piece{
    private static int [] POSSIBLE_MOVES = {-1,-7,-8,-9,1,7,8,9};
    public Queen(int position, PieceColor pieceColor) {
        super(position, pieceColor,PieceType.QUEEN);
    }

    @Override
    public Collection<Move> allLegalMoves(Board board) {
        int destPosition;
        List<Move> possibleMoves = new ArrayList<>();
        //loop through all the possible moves
        for (int po: POSSIBLE_MOVES){
            destPosition = this.position;
            //if its a valid position
            while(BoardUtils.legalTile(destPosition)){
                //if it breaks the offset rules
                if(inFirstCol(destPosition,po) || inEighthCol(destPosition,po)) {
                    break;
                }
                //add the offset
                destPosition += po;
                //if its still a possible position
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
                        //if there is any obstruction you cannot move past that point
                        break;
                    }
                }
            }
        }


        return possibleMoves;
    }
    private static boolean inFirstCol(int current, int offset) {
        return BoardUtils.COL_ONE[current] && ((offset == -9) || (offset == 7)|| (offset == -1));
    }
    private static boolean inEighthCol(int current, int offset) {
        return BoardUtils.COL_ONE[current] && ((offset == -7) || (offset == 9)||(offset == 1));
    }
    @Override
    public String toString(){
        return PieceType.QUEEN.toString();
    }

}
