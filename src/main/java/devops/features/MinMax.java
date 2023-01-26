package devops.features;

public class MinMax {
    private int minValue;
    private int maxValue;
    private int[] nums;
    
    public MinMax(int[] nums) {
        this.nums = nums;
        this.minValue = Integer.MAX_VALUE;
        this.maxValue = Integer.MIN_VALUE;
        this.find();
    }
    
    private void find() {
        for (int num : nums) {
            if(num < minValue)
                minValue = num;
            if (num > maxValue)
                maxValue = num;
        }
    }
    
    public int getMinValue() {
        return minValue;
    }
    
    public int getMaxValue() {
        return maxValue;
    }

}
