package Standard_Algorithms.tests;

import Standard_Algorithms.InsertionSort;
import java.util.Arrays;

public class TestInsertionSort
{
    public static void main(String[] args)
    {
        int[] testArray = new int[12];
        for (int i=0; i<12; i++)
            {
                testArray[i] = (int)(50*Math.random());
            }

        int[] testSorted = Arrays.copyOf(testArray, 12);
        InsertionSort.insertionSort(testSorted);

        int[] testLibrarySorted = Arrays.copyOf(testArray, 12);
        Arrays.sort(testLibrarySorted);

        if (!Arrays.equals(testSorted, testLibrarySorted))
            System.out.println("TEST FAILS");
        else
            System.out.println("test passes");
    }

}