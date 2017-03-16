# Internet-Tester

A simple and ugly script which tries to access google every 10 seconds until a successful request can be made.   
When a successful request is made, it will beep, and then start a speedtest.    
`chmod +x internet.py speedtest-cli`   
To run, simple: `./internet.py`   

Dependencies - "requests":  
`sudo apt install python3-pip -y && pip3 install requests`