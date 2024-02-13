public class Solution_169 {
    public static void main(String[] args){
        int[] input = {3,2,3};
        System.out.println("Result : " + majorityElement(input));
    }

    public static int majorityElement(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[j] < nums[i]){
                    int tmp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = tmp;
                }
            }
        }

        int result = nums[0];
        int max_count = 0;
        for (int i = 0; i < nums.length; i++){
            int a = nums[i];
            int count = 0;
            for(int j = i ; j < nums.length; j++){
                int b = nums[j];
                if (a == b){
                    count++;
                    if (count > max_count){
                        result = nums[j];
                        max_count = count;
                        count = 0;
                    }
                }
                else{
                    i = j-1;
                    break;
                }
            }
        }
        return result;
    }
}