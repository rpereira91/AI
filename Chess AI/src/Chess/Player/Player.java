package Chess.Player;

import Chess.Board.Board;
import Chess.Board.Move;
import Chess.PieceColor;
import Chess.Pieces.King;
import Chess.Pieces.Piece;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public abstract class Player {
    //keep track of the board
    protected Board board;
    protected King currentKing;
    protected Collection<Move> moves;
    private  boolean inCheck;

    public Player(Board board, Collection<Move> moves, Collection<Move> enemyMoves) {
        this.board = board;
        this.currentKing = crownKing();
        this.moves = moves;
        //does the opponents move attack the current players king's position, if the returned list is not empty the current player is in check
        this.inCheck = !Player.tileUnderAttack(this.currentKing.getPosition(), enemyMoves).isEmpty();
    }

    private static Collection<Move> tileUnderAttack(int position, Collection<Move> enemyMoves) {
        List<Move> attacks = new ArrayList<>();
        //if there are any moves that attack the position, add it to the list
        for(Move move: enemyMoves){
            if (position == move.getDestPos()){
                attacks.add(move);
            }
        }
        return attacks;
    }

    private King crownKing() {
        for (Piece p: getPieces())
            if (p.getPieceType().isKing())
                return (King) p;
        throw new RuntimeException("This is not a valid board");
    }
    //methods to check 
    public boolean legalMove(Move m){
        return this.moves.contains((m));
    }
    public boolean inCheck(){
        return this.inCheck;
    }
    public boolean inCheckMate(){
        return this.inCheck && !escapeMoves();
    }
    protected boolean escapeMoves(){
        for (Move m: this.moves){
            MoveTransition t = makeMove(m);
            if(t.getMoveStatus().isDone())
                return true;
        }
        return false;
    }
    public boolean inStalemate(){
        return false;
    }
    public boolean isCastled(){
        return false;
    }
    public MoveTransition makeMove(Move m){
        return null;
    }
    //helper methods to get
    public abstract Collection<Piece> getPieces();
    public abstract PieceColor getColor();
    public abstract Player getEnemy();
}
