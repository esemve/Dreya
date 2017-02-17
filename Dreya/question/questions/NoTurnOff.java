package dreya.question.questions;

import dreya.question.Question;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.Arrays;

/**
 *
 * @author smv
 */
public class NoTurnOff extends Question {
    
    public NoTurnOff(String sender, String message, String[] normalized)
    {
        if (
                (Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("kapcsolj")) | 
                (!Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("maradj") & Arrays.asList(normalized).contains("ebren")) |
                (Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("aludj")) |                       
                (Arrays.asList(normalized).contains("ne") & Arrays.asList(normalized).contains("menj") & Arrays.asList(normalized).contains("aludj"))
                
                
            )
        {
            this.hasAnswer = true;
        }
    }
    
    public String answer (String sender, String message, String[] normalized)
    {
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
              new FileOutputStream("noturnoff"), "utf-8"))) {
              writer.write("1");
        }
        catch (Exception ex) { }
        
        String[] answers = {"Rendben","Nem fogok kikapcsolni amíg nem szólsz","Bekapcsolva maradoks"};
        return randomAnswer(answers);
    }
}
