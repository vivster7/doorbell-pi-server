doorbell-pi-server
==================


#Setup on the Pi on Raspbian

    sudo apt-get update
    sudo apt-get install python-pip
    sudo pip install Flask

In order to get the audio through the audio output jack (instead of HDMI)
    
    sudo amixer cset numid=3 1

You can use:

    sudo amixer cset numid=3 2

to get the audio back through HDMI


