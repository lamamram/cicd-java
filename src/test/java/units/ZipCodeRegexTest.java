package units;

import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;
import com.example.helloworld.ZipCodeRegex;

public class ZipCodeRegexTest {
    private String zipCodePattern = "[0-9]{5}";
    private ZipCodeRegex zcr = new ZipCodeRegex(zipCodePattern);
    //nomenclature de méthode de test commençant par test, 
    // méthodes public sans retour car on exécute des assertions
    // décorateur Test (pour dire ici cas de test)
    @Test
    public void testMatch(){
        String zipcode = "44500";
        assertNotNull(zcr.match(zipcode));
    }
}
