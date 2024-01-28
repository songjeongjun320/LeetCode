import java.util.*;

public class Solution_347 {
    public static void main(String[] args){
        int[] nums = {1,1,2,2,2,3};
        int k = 2;
        for (int a : topKFrequent(nums, k)){
            System.out.println(a);
        }
    }

    public static int[] topKFrequent(int[] nums, int k) {
        ArrayList<int[]> data = new ArrayList<>();
        data.add(new int[]{nums[0], 1});

        for (int i = 1; i < nums.length; i++){
            int[] a = new int[2];
            boolean check = true;
            for (int j = 0; j < data.size(); j++){
                if (data.get(j)[0] == nums[i]){
                    int b = data.get(j)[1];
                    b++;
                    data.get(j)[1] = b;
                    check = false;
                    break;
                }
            }
            if (check){
                data.add(new int[]{nums[i], 1});
                check = false;
            }
        }

        for (int i = 0; i < data.size() - 1; i++){
            for (int j = i + 1; j < data.size() - 1; j++){
                int[] tmp;
                if (data.get(i)[1] < data.get(j)[1]){
                    tmp = data.get(i);
                    data.set(i, data.get(j));
                    data.set(j, tmp);
                }
            }
        }
        int[] result = new int[k];
        int count = 0;
        for (int[] arr : data){
            result[count++] = arr[0];
            if (count == k){
                break;
            }
        }
        return result;
    }
}