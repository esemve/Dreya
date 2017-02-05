package dreya;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

/**
 *
 * @author smv
 */
public class Database {
    
    public static HashMap map = new HashMap<String,String>();
    
    public static void save(String key, String value)
    {
        key = Database.md5(key);
        Database.map.put(key,value);

    }
            
    public static String get(String key, String defaultValue)
    {
        key = Database.md5(key);
        
        String value = (String) Database.map.get(key);
        
        if (value!=null)
        {
            return value;
        } else {
            return defaultValue;
        }
    }    
    
    public static void store()
    {
        try{
            FileOutputStream fos = new FileOutputStream(System.getProperty("user.dir")+"/database.ser",false);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(Database.map);
            oos.close();
         }catch(Exception e){
             System.out.println("[error] "+e.getMessage());
         }        
    }
    
    public static void restore()
    {
     
        System.out.println("[info] Working dir: "+System.getProperty("user.dir"));
        try{
            FileInputStream fis = new FileInputStream(System.getProperty("user.dir")+"/database.ser");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Database.map = (HashMap) ois.readObject();
            ois.close();        
        }catch(IOException | ClassNotFoundException e){
            System.out.println("[error] "+e.getMessage());
        }
    }
    
    public static String md5(String plaintext)
    {
        String hashtext = "";
        
        try
        {
            MessageDigest m = MessageDigest.getInstance("MD5");
            m.reset();
            m.update(plaintext.getBytes());
            byte[] digest = m.digest();
            BigInteger bigInt = new BigInteger(1,digest);
            hashtext = bigInt.toString(16);
            // Now we need to zero pad it if you actually want the full 32 chars.
            while(hashtext.length() < 32 ){
              hashtext = "0"+hashtext;
            }
        }
        catch (NoSuchAlgorithmException ex) {
            System.out.println("[error] "+ex.getMessage());
        }
        
        return hashtext;
    }
    
}
