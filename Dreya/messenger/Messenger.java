package dreya.messenger;


/**
 *
 * @author smv
 */
public class Messenger {
    
    public Messenger()
    {
    }
    

    public static void sendMessage(String recipient,String message)
    {
        Sender sender = new Sender();
        sender.send(recipient, message);
        //System.out.println(message);
    }
        
}
