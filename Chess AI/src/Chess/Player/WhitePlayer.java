package Chess.Player;

import Chess.Board.Board;
import Chess.Board.Move;
import Chess.PieceColor;
import Chess.Pieces.Piece;

import java.util.Collection;

public class WhitePlayer extends  Player{
    public WhitePlayer(Board board, Collection<Move> whiteLegalMoves, Collection<Move> blackLegalMoves) {
        super(board, whiteLegalMoves,blackLegalMoves);

    }

    @Override
    public Collection<Piece> getPieces(){
        return this.board.getWhite();
    }

    @Override
    public PieceColor getColor() {
        return PieceColor.WHITE;
    }

    @Override
    public Player getEnemy() {
        return this.board.blackPlayer();
    }
}
