// import java.util.*;

// class Hello{
//     public static void main(String[] args){
//         int arr[] = {3,5,2,6,6,9};
//         Deque<Integer> List = new ArrayDeque<>();
        
//         for(int i : arr){
//             List.addLast(i);
//         }

//         List.stream().map( x -> {
//             int y  = 0;
//             for(int i : arr){
//                 if(x < i){
//                     y = i;
//                     List.removeFirst();
//                     break;
//                 }
//                 y = -1;
//             }
//             return y;
//         }).forEach( i -> System.out.print(i+ " "));
//     }
// }

// import java.util.ArrayDeque;
// import java.util.Arrays;
// class Hello{
//     public static void main(String[] args){
//         int[] arr = {4,3,5,6,6,5};
//         System.out.print(Arrays.stream(arr).sum());
//         System.out.print(Arrays.stream(arr).sorted().distinct().forEach(System.out::println));
//     }
// }

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Hello{
    public static void main(String[] args){
        int[] arr = {2,3,5};
        ArrayDeque<Integer> List = new ArrayDeque<>();

        Arrays.stream(arr).map( x -> x * x ).forEach( i ->{ List.add(i);
            System.out.print(i+" ");
        } );
    }
}