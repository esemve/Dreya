package dreya.question;

import dreya.question.questions.*;
import java.util.ArrayList;

/**
 *
 * @author smv
 */
public class TextParser {
    
    String sender = "";
    String message = "";
    String[] normalized;
    ArrayList<Question> questions;
    
    public ArrayList<Question> getQuestions()
    {
        ArrayList<Question> newQuestions = new ArrayList<>();
        
        newQuestions.add(new Hello(this.sender,this.message,this.normalized));
        
        return newQuestions;
    }
    
    public TextParser(String sender, String message)
    {
        this.sender = sender;
        this.message = message;
        this.normalized = Normalizer.normalize(message);        
        this.questions = this.getQuestions();
        
    }

    public String getAnswer() {
        
        for (Question question: this.questions)
        {
            if (question.hasAnswer())
            {
                String answer = question.answer(this.sender,this.message,this.normalized);
                return answer;
            }
        }
        
        return "Sajnos nem értelek.";
    }
}
