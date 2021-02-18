"""
1. Shuffle - generate a random real number for each array entry
2. Srot the array

Shuffling - rearrange array so that the result is a uniformly random permutation in linear time


public class StdRandom
{
     public static void snuffle(Object[] a):
     {
         int N = a.length;
         for (int i = ; i < N ; i++)
         {
             int r = StdRandom.uniform(i + 1);
             exch(a, i, r)
         }
     }
}

"""
