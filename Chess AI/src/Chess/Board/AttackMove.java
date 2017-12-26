package Chess.Board;

import Chess.Pieces.Piece;
//this class is for moves that involve attacking
public class AttackMove extends Move {
    Piece attackedPiece;

    public AttackMove(Board board, Piece movedPiece, int destPosition, Piece attackedPiece) {
        super(board, movedPiece, destPosition);
        this.attackedPiece = attackedPiece;
    }
}
