# Project 4 Write Up

Name: Steven Cao
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
   - attach them to the private subnet
   - assign each instance a unique private IP within the private subnet
   - install webserver of choice on each instance
   - on each instance, change the hostname and Tag name to be unique for each system

## README.md documentation for configuration ( / 11)

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs  
   Description on how file is configured ( / 1)
2. Document how to SSH in between the systems utilizing their private IPs. ( / 1)
3. **_HAProxy configuration & documentation requirements_** ( / 3)
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
     - What configuration(s) were set (if any)
     - How to restart the service after a configuration change
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_** ( / 4)
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots. ( / 2)
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
