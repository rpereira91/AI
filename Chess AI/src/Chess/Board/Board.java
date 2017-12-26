package Chess.Board;

import Chess.PieceColor;
import Chess.Pieces.*;
import Chess.Player.BlackPlayer;
import Chess.Player.Player;
import Chess.Player.WhitePlayer;

import java.util.*;

public class Board {
    private List<Tile> chessBoard;
    private Collection<Piece> white;
    private  Collection<Piece> black;

    private WhitePlayer whitePlayer;
    private BlackPlayer blackPlayer;

    public Board(Builder b) {
        this.chessBoard = makeChessBoard(b);
        this.white = getActivePieces(this.chessBoard, PieceColor.WHITE);
        this.black = getActivePieces(this.chessBoard, PieceColor.BLACK);

        Collection <Move> whiteLegalMoves = calculateLegalMoves(this.white);
        Collection <Move> blackLegalMoves = calculateLegalMoves(this.black);

        this.whitePlayer = new WhitePlayer(this, whiteLegalMoves, blackLegalMoves);
        this.blackPlayer = new BlackPlayer(this, whiteLegalMoves, blackLegalMoves);

    }
    @Override
    public String toString(){
        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < BoardUtils.TILES; i++){
            String tileT = this.chessBoard.get(i).toString();
            builder.append(String.format("%3s", tileT));
            if((i + 1) % BoardUtils.RCTILES == 0){
                builder.append("\n");
            }
        }
        return builder.toString();
    }
    public Player whitePlayer(){
        return this.whitePlayer;
    }
    public Player blackPlayer(){
        return this.blackPlayer;
    }
    public Collection<Piece> getBlack() {
        return this.black;
    }
    public Collection<Piece> getWhite() {
        return this.white;
    }

    private Collection<Move> calculateLegalMoves(Collection<Piece> pieceColor) {
        List<Move> legalMoves = new ArrayList<>();
        for (Piece p: pieceColor){
            legalMoves.addAll(p.allLegalMoves(this));
        }

        return legalMoves;
    }

    //returns all the active pieces of a certain color
    private static Collection<Piece> getActivePieces(List<Tile> chessBoard, PieceColor color) {
        //a list to store all the pieces of the passed color
        List<Piece> pieces = new ArrayList<>();
        for(Tile t: chessBoard){
            if(t.tileOccupied()){
                Piece p = t.getPiece();
                if(p.getPieceColor() == color)
                    pieces.add(p);
            }

        }
        return pieces;
    }

    public Tile getTile(final int destPosition) {
        return chessBoard.get(destPosition);
    }

    //populates a list of tiles numbered 0-63
    private static  List<Tile> makeChessBoard(Builder b){
        Tile[] tiles = new Tile[BoardUtils.TILES];
        //from the builder we map a piece onto the tile ID
        for (int i = 0; i < BoardUtils.TILES; i++){
            //the tile ID will be whatever is on the "i" value
            tiles[i] = Tile.createTile(i,b.board.get(i));
        }
        return Arrays.asList(tiles);
    }
    //uses the builder class to build the chess board
    public static Board createStartingBoard(){
        Builder builder = new Builder();
        //sets each piece for the builder
        // sets the rooks
        builder.setPiece(new Rook(0, PieceColor.BLACK));
        builder.setPiece(new Rook(56,PieceColor.WHITE));
        builder.setPiece(new Rook(7,PieceColor.BLACK));
        builder.setPiece(new Rook(63,PieceColor.WHITE));

        //set the knights
        builder.setPiece(new Knight(1,PieceColor.BLACK));
        builder.setPiece(new Knight(62,PieceColor.WHITE));
        builder.setPiece(new Knight(6,PieceColor.BLACK));
        builder.setPiece(new Knight(57,PieceColor.WHITE));

        //sets the Bishops
        builder.setPiece(new Bishop(2,PieceColor.BLACK));
        builder.setPiece(new Bishop(5,PieceColor.BLACK));
        builder.setPiece(new Bishop(58,PieceColor.WHITE));
        builder.setPiece(new Bishop(61,PieceColor.WHITE));

        //sets the queens
        builder.setPiece(new Queen(3,PieceColor.BLACK));
        builder.setPiece(new Queen(59,PieceColor.WHITE));

        //sets the kings
        builder.setPiece(new King(4,PieceColor.BLACK));
        builder.setPiece(new King(60,PieceColor.WHITE));

        //since there are eight pawns we can use a for loop to place them
        for (int i = 8; i <= 15; i++){
            builder.setPiece(new Pawn(i,PieceColor.BLACK));
        }
        for (int i = 48; i <= 55; i++){
            builder.setPiece(new Pawn(i,PieceColor.WHITE));
        }
        //white to move
        builder.setNextMove(PieceColor.WHITE);
        //build the board
        return builder.build();
    }

    //create a builder class
    public static  class Builder{

        Map<Integer, Piece> board;
        PieceColor nextMove;

        public Builder(){
            this.board = new HashMap<>();
        }
        public Builder setPiece(Piece p){
            this.board.put(p.getPosition(),p);
            return this;
        }

        public Builder setNextMove(PieceColor pc){
            this.nextMove = pc;
            return this;
        }

        public Board build(){
            return new Board(this);
        }
    }
}
