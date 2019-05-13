import java.util.Scanner;



public class equilibriumhellconvert {

    public void henderson(boolean type) {
        if(type == false) {
            System.out.print("#  Enter a Ka value:  ");
            Scanner ka = new Scanner(System.in);
            ka.close();
            
        }
    }
    public static void main(String[] args) {
        boolean validResponse = false;
        System.out.println("#  WELCOME TO THE QUILIBRIUM HELL CALCULATOR. Ver. 0.8.9");
        System.out.println("1: Calculate pOH of a buffer from Kb (Henderson Hasselbalch equation) \n2: Calculate the pH of a buffer from Ka (Henderson Hasselbalch equation)\n3: Calculate the ratio of a base/acid from pH and Ka\n4: Calculate the ratio of acid/base from pOH and Kb\n5: Solve an ICE table");
        System.out.print("#  What would you like to do? (Type 'exit' to exit):  ");
        Scanner input = new Scanner(System.in);
        String choice = input.toString();
        input.close();
        switch (choice) {
            case "1":
                validResponse = true;
                System.out.println(" ");

                break;
        
            case "2":

                break;
            
            case "3":

                break;

            case "4":

                break;

            case "5":
            
                break;
            
            case "exit":

                return;

            default:
                break;
        }
    }
}