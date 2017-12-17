package Chess.Board;

import Chess.Pieces.Piece;
//this class is if a piece needs to move to a tile not obstructed by a piece
public class NonAttackMove extends Move {
    public NonAttackMove(Board board, Piece movedPiece, int destPosition) {
        super(board, movedPiece, destPosition);
    }
}
