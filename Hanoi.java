package Lab5;
//programmers: Ronin Sloan, Tuan Le
//Lab 5 towers of hanoi
//date: 2/16/23
//purpose: create a program that can solve the towers of hanoi puzzle.
public class Hanoi {
    public static void main(String[] args) {
        int plate = 4;
        tower(plate, "1", "2", "3");
    }

    static void tower(int plate, String tower1, String tower2, String tower3){
        if(plate == 0){
            return;
        }
        tower(plate - 1, tower1, tower3, tower2);
        System.out.println("Move plate " + plate + " from tower" + tower1 + 
        " to tower" + tower2);
        tower(plate - 1, tower3, tower2, tower1);
    }
}
