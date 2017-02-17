package dreya.security;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Random;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

/**
 *
 * @author smv
 */
public class Mp3Player implements Runnable {
    
    
    public static String[] files;
    
    public void run()
    {
        
        int rnd = new Random().nextInt(files.length);
        String file = files[rnd];
        
        try{
            FileInputStream fis = new FileInputStream("mp3/"+file);
            Player playMP3 = new Player(fis);
            playMP3.play();

            }
         catch(FileNotFoundException | JavaLayerException e){System.out.println("[error] "+e.getMessage());}        
    }
    
}
