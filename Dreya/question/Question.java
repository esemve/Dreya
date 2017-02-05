package dreya.question;

/**
 *
 * @author smv
 */
public class Question {
    
    public boolean hasAnswer;
    public boolean hasRequestion = false;
    
        
    public String randomAnswer(String[] answers)
    {
        return answers[0];
    }
    
    public boolean hasAnswer()
    {
        return this.hasAnswer;
    }

    public String answer(String sender, String message, String[] normalized) {
        return ".";
    }


}
