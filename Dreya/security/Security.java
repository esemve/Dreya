package dreya.security;

import dreya.messenger.Messenger;
import java.util.Calendar;
import dreya.serial.SerialReader;
import java.io.InputStream;
import dreya.Config;
import java.net.URL;
import java.net.URLConnection;


/**
 *
 * @author smv
 */
public class Security implements Runnable {


    private long key1 = 0;
    private long key2 = 0;
    private long newKey1 = 0;
    private long newKey2 = 0;
    private long motion = 0;
    private long whoAreYou = 0;
    private boolean armed = false;
    private boolean camera = true;
    
    @Override
    public void run() {

        this.key1 = time()+1;
        this.key2 = time()+1;
        this.newKey1 = time()+1;
        this.newKey2 = time()+1;        
        
        while (true)
        {
            Calendar now = Calendar.getInstance();
            int hour = now.get(Calendar.HOUR_OF_DAY);
            int min = now.get(Calendar.MINUTE);
            int sec = now.get(Calendar.SECOND);            
            long time = time();

            if ("1".equals(SerialReader.key1))
            {
                this.newKey1 = time();
                this.closeCamera();
            } 
            
            if ("1".equals(SerialReader.key2))
            {
                this.newKey2 = time();
                this.closeCamera();
            } 
            
            try
            {
                Thread.sleep(1000);
            }
            catch (Exception ex) { }
            
            if ((newKey1<time()-300) & (newKey2<time()-300))
            {
                if (!this.armed)
                {
                    if (hour>8)
                    {
                        Messenger.sendMessage("", "Riasztó aktív!");

                        String[] mp3Sentry = new String[1];
                        mp3Sentry[0] = "sentry.mp3";
                        this.playSound(mp3Sentry);                    
                    }
                }
                this.armed = true;
            }
            
            if ((this.newKey1==time) & (this.newKey1>this.key1+1))
            {
                if (this.armed)
                {
                    Messenger.sendMessage("", "Kulcs #1 behelyezve.");
                }
            }
            if ((this.newKey2==time) & (this.newKey2>this.key2+1))
            {
                if (this.armed)
                {
                    Messenger.sendMessage("", "Kulcs #2 behelyezve.");
                }
            }
            
            
           
            
            if (((this.newKey1==time-2) & (this.newKey1==this.key1)) | ((this.newKey2==time-2) & (this.newKey2==this.key2)))
            {
                if ((hour<22) & (hour>8))
                {
                    String[] mp3Bye = new String[2];
                    mp3Bye[0] = "goodbye.mp3";
                    mp3Bye[1] = "goodbye2.mp3";
                    this.playSound(mp3Bye);
                }
                
                if ((this.newKey1<time) & (this.newKey2<time))
                {
                        this.openCamera();
                }
            }
            
            
            if (((this.newKey1==time) & (this.newKey1>this.key1+3)) | ((this.newKey2==time) & (this.newKey2>this.key2+3)))
            {
                if ((hour<22) & (hour>8))
                {
                    String[] mp3Hello = new String[3];
                    mp3Hello[0] = "hello.mp3";
                    mp3Hello[1] = "hello2.mp3";
                    mp3Hello[2] = "hello3.mp3";
                    this.playSound(mp3Hello);
                }
                this.armed = false;                
            }
            
            if (SerialReader.motion)
            {
                this.motion = time;
            }
            
            if ((this.armed) & (this.motion>time-3))
            {
                if (this.whoAreYou<time-15)
                {
                    this.whoAreYou = time;
                    String[] mp3Alert1 = new String[1];
                    mp3Alert1[0] = "alert.mp3";
                    this.playSound(mp3Alert1);                    
                    Messenger.sendMessage("", "Mozgás a lakásban!");
                }
                
                if ((this.whoAreYou<time-5) & (this.whoAreYou>time-15))
                {
                    String[] mp3Alert2 = new String[1];
                    mp3Alert2[0] = "alert2.mp3";
                    this.playSound(mp3Alert2);
                    
                    this.playSound2(mp3Alert2);                    
                    
                    this.playSound3(mp3Alert2);
                }
            }
            
            this.key1 = this.newKey1;
            this.key2 = this.newKey2;

        }
    }
    
    private long time()
    {
        return System.currentTimeMillis() / 1000L;
    }
    
    public void playSound(String[] files)
    {
        Mp3Player.files = files;
        
        try
        {
            Mp3Player player = new Mp3Player();
            Thread mp3PlayerThread = new Thread(player);
            mp3PlayerThread.start();
        }
        catch (Exception ex)
        {
            System.out.println("[error] mp3 lejátszás nem sikerült!");
        }
    }
    
    public void playSound2(String[] files)
    {
        Mp3Player.files = files;
        
        try
        {
            Mp3Player player = new Mp3Player();
            Thread mp3PlayerThread2 = new Thread(player);
            mp3PlayerThread2.sleep(300);
            mp3PlayerThread2.start();
        }
        catch (Exception ex)
        {
            System.out.println("[error] mp3 lejátszás nem sikerült!");
        }
    }    
    
    public void playSound3(String[] files)
    {
        Mp3Player.files = files;
        
        try
        {
            Mp3Player player = new Mp3Player();
            Thread mp3PlayerThread2 = new Thread(player);
            mp3PlayerThread2.sleep(500);
            mp3PlayerThread2.start();
        }
        catch (Exception ex)
        {
            System.out.println("[error] mp3 lejátszás nem sikerült!");
        }
    }      
    

    
    public void closeCamera() {
        try
        {
            if (this.camera)
            {
                URL url = new URL("http://"+Config.cameraIp+":81/web/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=7");
                URLConnection uc = url.openConnection();

                String userpass = Config.cameraUserPass;
                String basicAuth = "Basic " + userpass;

                uc.setRequestProperty ("Authorization", basicAuth);
                InputStream in = uc.getInputStream();
                this.camera = false;
            }

        }
        catch (Exception ex)
        {
            System.out.println("[error] "+ex.getMessage());
        }
    }
    
    public void openCamera()
    {
        try
        {            
            if (!this.camera)
            {
                URL url = new URL("http://"+Config.cameraIp+":81/web/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=0");
                URLConnection uc = url.openConnection();

                String userpass = Config.cameraUserPass;
                String basicAuth = "Basic " + userpass;

                uc.setRequestProperty ("Authorization", basicAuth);
                InputStream in = uc.getInputStream();
                this.camera = true;
            }
        }
        catch (Exception ex)
        {
            System.out.println("[error] "+ex.getMessage());
        }
    }
    
}
