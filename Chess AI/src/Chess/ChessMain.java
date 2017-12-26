package Chess;

import Chess.Board.Board;

public class ChessMain {
    public static void main(String[] args) {
        Board board = Board.createStartingBoard();
        System.out.println(board);

    }
}
