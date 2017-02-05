package dreya.question;

import java.util.List;

/**
 *
 * @author smv
 */
public class Normalizer {
    
    
    public static List<String> words;
    
    public static String normalizeWords(String message)
    {   
        message = Normalizer.normalizeSingleWords(message, "hello|szia|szerbusz|szervusz|csao|haliho|jo estet|joestet|joreggelt|jo napot");
        
        return message;
    }
    
    public static String[] normalize(String message)
    {
        message = message.toLowerCase();
        
        String[] replaceFrom = {"á","é","í","ó","ö","ő","u","ú","ü","ű",".",":","!","?","'",","};
        String[] replaceTo = {"a","e","i","o","o","o","u","u","u","u"," "," "," "," "," "," "};
        
        for(int i = 0; i < replaceFrom.length; i++)
        {
            message = message.replace(replaceFrom[i], replaceTo[i]);
        }
        
        
        message = Normalizer.normalizeWords(message);
        
        String[] messageParts =  message.split(" ");
        return messageParts;
    }
    
    public static String normalizeSingleWords(String message, String wordlist)
    {
        
        wordlist = wordlist+"|";
        String[] list = wordlist.split("\\|");
        String to = list[0];
        
        for(String norm: list )
        {
            message = message.replace(norm, to);
        }
        
        return message;
    }
    
}
