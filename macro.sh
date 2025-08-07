xdotool mousemove 1479 328
xdotool click 1
xdotool key ctrl+a
xdotool key ctrl+c
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Tab
xdotool key Return 
xdotool sleep 0.25
xdotool mousemove 1672 398
xdotool click 2
xdotool sleep 0.25
xdotool mousemove 1687 728
xdotool click 2
xdotool key Return
xdotool sleep 0.25
xdotool key Return
xdotool mousemove 246 156
xdotool click 1
xdotool mousemove 290 443
xdotool click 1
xdotool mousemove 641 454
xdotool click 1
sleep 1.5
xdotool mousemove 515 690
sleep 2.5
xdotool click 1
xdotool key Return
sleep 0.5
xdotool key Return
xdotool key tab
xdotool key ctrl+v
xdotool mousemove 175 1058
xdotool click 1
cd ~/Desktop/twsearch1/samples/main
nano 7x7L2C.scr
cd ~/Desktop/twsearch1
./build/bin/twsearch -M 1500 --noedges --alloptimal --microthreads 4 --startprunedepth 4 --mindepth 7 --maxdepth 17 --nowrite --nocorners --moves 2L,L,F,R,U,2R,3L,3R samples/main/7x7x7.tws samples/main/7x7L2C.scr
done
