package Chess;
//type safe way to store the colors, since we have two instances of possible colors
public enum PieceColor {
    WHITE {
        @Override
        public int direction() {
            return -1;
        }

        @Override
        public boolean isBlack() {
            return false;
        }

        @Override
        public boolean isWite() {
            return true;
        }
    },
    BLACK {
        @Override
        public int direction() {
            return 1;
        }

        @Override
        public boolean isBlack() {
            return true;
        }

        @Override
        public boolean isWite() {
            return false;
        }
    };
    //directional switch for colors
    public abstract int direction();

    public abstract boolean isBlack();

    public abstract boolean isWite();
}
