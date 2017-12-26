package Chess.Pieces;

import Chess.Board.*;
import Chess.PieceColor;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Pawn extends  Piece{
    private static int [] POSSIBLE_MOVES = {7,8,9,16};
    public Pawn(int position, PieceColor pieceColor) {
        super(position, pieceColor,PieceType.PAWN);
    }

    @Override
    public Collection<Move> allLegalMoves(Board board) {
        int destPosition;
        List<Move> possibleMoves = new ArrayList<>();
        for (int po: POSSIBLE_MOVES){
            //get direction to see if we're moving +8 tiles or -8 tiles
            destPosition = this.position + (this.getPieceColor().direction() * po);
            if (!BoardUtils.legalTile(destPosition))
                continue;
            //non attacking pawn move
            if(po == 8 && board.getTile(destPosition).tileOccupied())
                possibleMoves.add(new NonAttackMove(board,this,destPosition));
            //checking if it's the first move for the double jump, we also need to check if it's black or white (as it will effect the rows check)
            else if (po == 16 && this.firstMove() && BoardUtils.ROW_TWO[this.position] && this.pieceColor.isBlack()
                    || BoardUtils.ROW_SEVEN[this.position] && this.pieceColor.isWite()){
                int behindDestPosition = this.position + (this.pieceColor.direction() * 8);
                if (!board.getTile(behindDestPosition).tileOccupied() &&
                        !board.getTile(destPosition).tileOccupied()){
                    possibleMoves.add(new NonAttackMove(board,this,destPosition));
                }
                //diagonal attacking
                // if the pawn is in the eighth column and attempts to attack diagonally to 7 and is white it won't work
                //same as if the pawn is in the first column and is black, since the offset for 7 will put it on the same row
                else if (po == 7 && !(BoardUtils.COL_EIGHT[this.position] && this.pieceColor.isWite()
                        || (BoardUtils.COL_ONE[this.position] && this.pieceColor.isBlack() ))){
                    if(board.getTile(destPosition).tileOccupied()){
                        Piece possiblePiece = board.getTile(destPosition).getPiece();
                        //if the colors are different add it to the attack move list
                        if(this.pieceColor != possiblePiece.pieceColor){
                            possibleMoves.add(new AttackMove(board,this,destPosition,possiblePiece));
                        }
                    }
                }//Opposite columns for black and white
                else if (po == 9 && !(BoardUtils.COL_EIGHT[this.position] && this.pieceColor.isBlack()
                        || (BoardUtils.COL_ONE[this.position] && this.pieceColor.isWite() ))){
                    Piece possiblePiece = board.getTile(destPosition).getPiece();
                    //if the colors are different add it to the attack move list
                    if(this.pieceColor != possiblePiece.pieceColor){
                        possibleMoves.add(new AttackMove(board,this,destPosition,possiblePiece));
                    }
                }
            }
        }

        return possibleMoves;
    }
    @Override
    public String toString(){
        return PieceType.PAWN.toString();
    }
}
