package Chess.Board;

import Chess.Pieces.Piece;

public abstract class Move {

    Board board;
    Piece movedPiece;
    int destPosition;

    Move(Board board, Piece movedPiece, int destPosition) {
        this.board = board;
        this.movedPiece = movedPiece;
        this.destPosition = destPosition;
    }

    public int getDestPos() {
        return destPosition;
    }
}
