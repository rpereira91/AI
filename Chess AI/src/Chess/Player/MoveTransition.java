package Chess.Player;

import Chess.Board.Board;
import Chess.Board.Move;

import java.util.concurrent.Future;

public class MoveTransition {
    private Board tranBoard;
    private Move m;
    private MoveStatus ms;

    public MoveTransition(Board tranBoard, Move m, MoveStatus ms) {
        this.tranBoard = tranBoard;
        this.m = m;
        this.ms = ms;
    }

    public MoveStatus getMoveStatus() {
        return this.ms;
    }
}
