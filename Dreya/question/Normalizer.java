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
        message = Normalizer.normalizeSingleWords(message, "mi|micsoda");
        message = Normalizer.normalizeSingleWords(message, "elet|elet|vilagmindenseg|vilag");
        message = Normalizer.normalizeSingleWords(message, "ertelme|ertelme");
        message = Normalizer.normalizeSingleWords(message, "ne|ne");
        message = Normalizer.normalizeSingleWords(message, "nem|nem");
        message = Normalizer.normalizeSingleWords(message, "kapcsolj|kikapcs|kapcsolodj");
        message = Normalizer.normalizeSingleWords(message, "ebren|ebren");
        message = Normalizer.normalizeSingleWords(message, "maradj|maradj");
        message = Normalizer.normalizeSingleWords(message, "menj|menj|mehetsz");
        message = Normalizer.normalizeSingleWords(message, "ki|ki");
        message = Normalizer.normalizeSingleWords(message, "aludj|aludhatsz|aludj|alvas|aludni");
        
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
