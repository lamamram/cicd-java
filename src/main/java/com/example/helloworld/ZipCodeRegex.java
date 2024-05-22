package com.example.helloworld;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ZipCodeRegex {
    private Pattern pattern;

    public ZipCodeRegex(String patternString){
        this.pattern = Pattern.compile((patternString));
    }

    public String match(String target){
        String ret = null;
        Matcher matcher = pattern.matcher(target);
        if(matcher.find()){
            ret = matcher.group();
        }
        return ret;
    }

}
