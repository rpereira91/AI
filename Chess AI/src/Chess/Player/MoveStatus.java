package Chess.Player;

public enum MoveStatus {
    DONE {
        @Override
        boolean isDone() {
            return true;
        }
    };
    abstract boolean isDone();
}
