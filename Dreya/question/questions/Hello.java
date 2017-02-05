package dreya.question.questions;

import dreya.question.Question;
import java.util.Arrays;

/**
 *
 * @author smv
 */
public class Hello extends Question {

    public Hello(String sender, String message, String[] normalized)
    {
        if (Arrays.asList(normalized).contains("hello"))
        {
            this.hasAnswer = true;
        }
    }
    
    public String answer (String sender, String message, String[] normalized)
    {
        String[] answers = {"Szia!","Hello!",":)!","Re","Csaó","Szerbusz"};
        return randomAnswer(answers);
    }
    
}
