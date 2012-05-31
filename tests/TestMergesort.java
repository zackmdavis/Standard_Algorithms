package Standard_Algorithms.tests;

import Standard_Algorithms.Mergesort;
import java.util.Arrays;

public class TestMergesort
{
    public static void main(String[] args)
    {
        float[] testArray = new float[6];
        for (int i=0; i<6; i++)
            {
                testArray[i] = (float)(20*Math.random());
            }

        float[] testSorted = Arrays.copyOf(testArray, 6);
        Mergesort.mergesort(testSorted, 0, 5);
        
        float[] testLibrarySorted = Arrays.copyOf(testArray, 6);
        Arrays.sort(testLibrarySorted);

        if (Arrays.equals(testSorted, testLibrarySorted))
            {
                System.out.println("test passes");
                System.out.println(Arrays.toString(testArray));
                System.out.println(Arrays.toString(testSorted));
            }
        else
            {
                System.out.println("test fails");
                System.out.println(Arrays.toString(testArray));
                System.out.println(Arrays.toString(testSorted));
            }
    }

}