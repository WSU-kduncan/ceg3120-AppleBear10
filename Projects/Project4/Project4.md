# Project 4 Write Up

Name: Steven Ca

Email: cao.19@wright.edu

## CloudFormation template
   - Made multiple changes to the cloud formation template to fit the requirements.
   - Took note of the subnet range for CidrBlock: 10.0.0.0/24 to be from 10.0.0.4/24 - 10.0.0.255. Same with CidrBlock: 10.0.1.0/24 to be from 10.0.1.7/24 - 10.0.1.255
   - Added a home ip address under SecurityGroupIngress: CidrIp: 98.29.55.9/32
   - Under ProxyInstance: I added a haproxy installation.
     - apt-get install -y \
     - haproxy && \ (note I used && because it was the last installation and there was a new command after it)
   - Made two unique PrivateIpAddresses for WebServ1Instance (10.0.1.10) and WebServ2Instance (10.0.1.9)
   - Installed apache2 on both WebServInstances
     - apt-get install -y \
     - apache2 && \ (Used && for the same reason above)
   - Added a hostname by doing:
     - hostnamectl set-hostname "ceg3120s1-s2" && \

## For the pool of content servers:
   - create two total backend host instances
     - in /etc/hosts added:
     - Attached them to a private subnet


![backend-servers](https://cdn.discordapp.com/attachments/811148913523687434/1036821148970795158/unknown.png)
   - install webserver of choice on each instance
     - Installed apache2 web servers
   - on each instance, change the hostname and Tag name to be unique for each system
     - Specified which is proxy, server1, and server2 instance
[Server-help](https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/)


## README.md documentation for configuration 

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs  
     - sudo vim /etc/hosts
     - added the following requirements that correlates to hostnames to private IPs



![Requirements](https://cdn.discordapp.com/attachments/811148913523687434/1036823921846140998/unknown.png)

2. Document how to SSH in between the systems utilizing their private IPs.
     - sudo ~/.ssh/config
     - Added two hosts that correlated to the corresponding servers with their specified private IPs
     - The picture below shows how to do so


![Requirements](https://cdn.discordapp.com/attachments/811148913523687434/1036824229334753331/unknown.png)



     - Once you have set that up you can ssh into proxy first and then switch to either servers with commands:
     - ssh -i /home/scao/ceg3120-AppleBear10/ceg3120key.pem ubuntu@10.0.1.10 (Server1)
     - ssh -i /home/scao/ceg3120-AppleBear10/ceg3120key.pem ubuntu@10.0.1.9 (Server2)

3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - 1. Assuming HAproxy was installed successfully we can first cat /etc/haproxy/ for existence
     - 2. cat /etc/haproxy/haproxy.cfg to confirm it's there
     - 3. sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bak for back up incase anything goes wrong
     - 4. go into the specified path and under "global" add maxconn for max number of connections to frontend and pool
     - 5. add a frontend label and paste the public ip
     - 6. curl ipinfo.io for information on ip and bind 10.0.0.10:80 by using command "ip a" to find private ip
     - 7. under that create default_backend Web_Servers and create label underneath that with backend Web_Servers
     - 8. after labels are created make a "balance round robin" so in order to hit refresh and see where content got redirected
     - 9. add option httpchk HEAD to see if sites up
     - 10. then add servers... server serv1 10.0.1.10:80 and server serv2 10.0.1.9:80
     - Resources used (website link below)
[Website-link](https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/)
4. **_Webserver 1 & 2 configuration & documentation_**
   - How set up a webserver
     - Files that were modified were /etc/hosts so that hostname could be added for entry for HAproxy servers
     - Needed to install apache2 web service with command: sudo apt install apache2
     - Then you needed to enable with: sudo systemctl enable apache2
     - After that is done you can start it with: sudo systemctl start apache2
     - Once that is done you can create an index file for web server 1 with: $echo < H1 >Hello! This is webserver1: 10.0.1.9< /H1 > | sudo tee /var/ww/html/indexsrv1.html
     - Make sure to add the correct .html file provided by the professor and chmod 400 the file
     - Repeat the steps for web server 2
     - One that is done make sure to configure haproxy or check if it's working
     - You can do commands like "haproxy -c -f /etc/haproxy/haproxy.cfg" to show that the configurations are correct
     - You can get the status with: "sudo systemctl status haproxy.cfg" which shows the active (running) status meaning HAproxy is enabled and running fine
     - To finally apply the configuration you can do the command: sudo systemctl restart haproxy.service
     - The command above will stop and then start the HAproxy service
     
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
![Server1](https://cdn.discordapp.com/attachments/811148913523687434/1036805836623855698/unknown.png)
   - one screenshot that shows content from "server 2"
![Server2](https://cdn.discordapp.com/attachments/811148913523687434/1036805924871995402/unknown.png)
