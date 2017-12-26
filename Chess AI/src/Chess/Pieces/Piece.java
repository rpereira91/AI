package Chess.Pieces;

import Chess.Board.Board;
import Chess.Board.Move;
import Chess.PieceColor;

import java.util.Collection;

public abstract class  Piece{

    protected int position;
    protected PieceColor pieceColor;
    protected boolean firstMove;
    protected PieceType pt;

    public Piece(final int position, final PieceColor pieceColor,PieceType pt) {
        this.position = position;
        this.pieceColor = pieceColor;
        this.firstMove = false;
        this.pt = pt;
    }
    //contains a collection of legal moves from a board passed into it
    public abstract Collection<Move> allLegalMoves(final Board board);
    public PieceColor getPieceColor(){
        return this.pieceColor;
    }
    public boolean firstMove(){return this.firstMove;}
    public int getPosition(){
        return position;
    }
    public PieceType getPieceType(){
        return this.pt;
    }

    public enum PieceType{

        PAWN("P") {
            @Override
            public boolean isPawn() {
                return true;
            }

            @Override
            public boolean isBishop() {
                return false;
            }

            @Override
            public boolean isRook() {
                return false;
            }

            @Override
            public boolean isKing() {
                return false;
            }
        },
        KNIGHT("N") {
            @Override
            public boolean isPawn() {
                return false;
            }

            @Override
            public boolean isBishop() {
                return false;
            }

            @Override
            public boolean isRook() {
                return false;
            }

            @Override
            public boolean isKing() {
                return false;
            }
        },
        BISHOP("B") {
            @Override
            public boolean isPawn() {
                return false;
            }

            @Override
            public boolean isBishop() {
                return true;
            }

            @Override
            public boolean isRook() {
                return false;
            }

            @Override
            public boolean isKing() {
                return false;
            }
        },
        ROOK("R") {
            @Override
            public boolean isPawn() {
                return false;
            }

            @Override
            public boolean isBishop() {
                return false;
            }

            @Override
            public boolean isRook() {
                return true;
            }

            @Override
            public boolean isKing() {
                return false;
            }
        },
        QUEEN("Q") {
            @Override
            public boolean isPawn() {
                return false;
            }

            @Override
            public boolean isBishop() {
                return false;
            }

            @Override
            public boolean isRook() {
                return false;
            }

            @Override
            public boolean isKing() {
                return false;
            }
        },
        KING("K") {
            @Override
            public boolean isPawn() {
                return false;
            }

            @Override
            public boolean isBishop() {
                return false;
            }

            @Override
            public boolean isRook() {
                return false;
            }

            @Override
            public boolean isKing() {
                return true;
            }
        };
        private String pName;
        PieceType(String pName){
            this.pName = pName;
        }
        @Override
        public String toString(){
            return this.pName;
        }
        public abstract boolean isPawn();
        public abstract boolean isBishop();
        public abstract boolean isRook();
        public abstract boolean isKing();
    }

}
