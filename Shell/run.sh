result=`ps aux | grep -i "Dreya" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        echo "Dreya is already running"
   else
        echo "Starting Dreya..."
        java -cp Dreya.jar dreya.Dreya
    fi
