package devops.units;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import devops.features.MinMax;

class MinMaxTest {
    private MinMax mm;

    @Test
    void test() {
        // section "Arrange": contexte
        int[] nums = {1,2,-66,384};
        mm = new MinMax(nums);
        
        // section "Act": calcul
        int minValue = mm.getMinValue();
        int maxValue = mm.getMaxValue();
        
        // section "Assert": calculé vs attendu
        assertEquals(minValue, -66);
        assertEquals(maxValue, 384);
    }

}
