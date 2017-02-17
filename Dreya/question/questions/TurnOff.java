package dreya.question.questions;

import dreya.question.Question;
import java.io.File;
import java.util.Arrays;
import java.util.Calendar;

/**
 *
 * @author smv
 */
public class TurnOff extends Question {
    
    public TurnOff(String sender, String message, String[] normalized)
    {
        if (
                (!Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("aludj")) | 
                (!Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("menj")) | 
                (!Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("kapcsolj") & Arrays.asList(normalized).contains("ki"))
            )
        {
            this.hasAnswer = true;
        }
    }
    
    public String answer (String sender, String message, String[] normalized)
    {
        try {
                File f = new File("noturnoff");
                if(f.exists() && !f.isDirectory()) { 
                        f.delete();
                }        
        }
        catch (Exception ex) { }
        
        Calendar now = Calendar.getInstance();
        int hour = now.get(Calendar.HOUR_OF_DAY);
        
        if (hour<=23)
        {
            String[] answers = {"Rendben, éjfélkor megyek alukálni","Megyek aludni amint letelt a nap","Rendben, este alszom"};
            return randomAnswer(answers);
        }
        else
        {
            String[] answers = {"Rendben","Megyek aludni","Szép álmokat!"};    
            return randomAnswer(answers);
        }
    }
}
