# Internet-Tester

While backpacking through Asia, I noticed the internet could suddenly disapear. Sometimes it would come back 30 seconds later, sometimes 2 hours later. To avoid having to baby-sit the computer, I wrote this script. 

The idea is that you start the script (./internet.py) when you loose the internet, and it it will try to connect to the internet every 10 seconds. When it's connected, it does a few beeping sound and tests the internet connection.

Requires colorama (pip3 install colorama)
