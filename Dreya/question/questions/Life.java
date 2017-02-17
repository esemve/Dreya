package dreya.question.questions;

import dreya.question.Question;
import java.util.Arrays;

/**
 *
 * @author smv
 */
public class Life extends Question {
    
    public Life(String sender, String message, String[] normalized)
    {
        if (Arrays.asList(normalized).contains("mi") & Arrays.asList(normalized).contains("elet")  & Arrays.asList(normalized).contains("ertelme"))
        {
            this.hasAnswer = true;
        }
    }
    
    public String answer (String sender, String message, String[] normalized)
    {
        String[] answers = {"42"};
        return randomAnswer(answers);
    }
}
