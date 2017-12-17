package Chess.Player;

import Chess.Board.Board;
import Chess.Board.Move;
import Chess.PieceColor;
import Chess.Pieces.Piece;

import java.util.Collection;

public class BlackPlayer extends Player{
    public BlackPlayer(Board board, Collection<Move> whiteLegalMoves, Collection<Move> blackLegalMoves) {
        super(board, blackLegalMoves,whiteLegalMoves);

    }

    @Override
    public Collection<Piece> getPieces(){
        return this.board.getBlack();
    }

    @Override
    public PieceColor getColor() {
        return PieceColor.BLACK;
    }

    @Override
    public Player getEnemy() {
        return this.board.whitePlayer();
    }

}
