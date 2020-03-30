import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Main{

    private static int findLongestSeq(Integer[] arr){
        // I. ...
        ArrayList<Integer> seq = new ArrayList<>();
        int counter = 0;

        // II. ...
        for (int i=0; i<arr.length; i++){
            if (arr[i] == 1){
                counter++;
                if (counter > 0 && i == arr.length-1){
                    seq.add(counter);
                }
            }else{
                if (counter > 0){
                    seq.add(counter);
                }
                seq.add(arr[i]); // A.1.
                // seq.add(1); // B.1
                counter = 0;
            }
        }

        // III. ...
        int longestSeq = 0;
        for (int i=0; i<seq.size(); i=i+2){
            int t = seq.get(i);
            if (i+1 < seq.size()){
                t += 1; // A.2.
                // t += seq.get(i+1); // B.2.
            }
            if (i+2 < seq.size()){
                t += seq.get(i+2);
            }
            if (longestSeq < t){
                longestSeq = t;
            }
        }


        // IV. ...
        System.out.println("Input : " +  Arrays.asList(arr));
        System.out.println(seq);
        System.out.println("Max sequence : " + longestSeq);
        System.out.println("\n\n\n");

        return longestSeq;
    }


    public static void main(String[] args){
        System.out.println("Hello No. 1");

        // ...
        // int[] arr = {1,1,0,1,1,0,1};
        Integer[] arr = new Integer[] {1,1,0,1,1,0,1}; // 5
        int longestSeq = findLongestSeq(arr);

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,0,1,0,1,0,1,0,1}); //

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,1,0,1,1}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,1,0,1,1,0}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,1,1,0,1,1}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,1,0,0}); // 2

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,0,0,1,1,1,0,0}); // 4

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0}); // 6

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1}); // 8

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,1,0,1,1,0,1,1,1}); // 6

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,1,1,0,1,1,0,1,1}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,1,0,1,1,0,1,1,0}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,1,1,0,1,1,0,1,1,0}); // 5

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,0,0,1,1,0,1,1,0,1,1,1}); // 6

        // ...
        longestSeq = findLongestSeq(new Integer[] {1,1,0,1,1,0,1,1,1,0,0,0,0}); // 6

        // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0}); // 6

        // // ...
        longestSeq = findLongestSeq(new Integer[] {0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0}); // 4

    }
}