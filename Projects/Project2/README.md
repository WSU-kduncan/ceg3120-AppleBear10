# Project 2

## Objectives:

- Understand and build a private cloud network
- Understand and build an EC2 instance

## Assignment Notes / Hints

For this project you need access to your AWS console. [Return to here and click "Start Lab"](https://awsacademy.instructure.com/courses/24169/modules/items/1983042).

**Once the icon next to "AWS" is green, click "AWS" to open the console.**

Create a `Project2` folder in your GitHub Classrooms repo. This project is mostly documentation of work, so you are welcome to work on your documentation and in your repo wherever you are comfortable. I would float towards VSCode myself.

In your `Project2` folder, create a file named `README.md` Do you work for Parts 1 & 2 here.

- It will be handy, but not necessary, to compare / contrast the resources you are making with the working "stack" you have. That stack is based on a template, and that template defined all of these resources - and worked.
- When asked to create "tags", you want to make a "Name" tag and then write the name in the value field. Sometimes the "Name" tag will be auto-filled for you. Sometimes not.
- If you get to a point where you need to start over, carefully go through and delete the resources you have already created.
  1. This is good maintenance. Leaving behind junk is frowned upon in any industry
  2. This will keep you from running resources you can be charged for (like unused instances and elastic IPs)

## Part 1 - Build a VPC

For each step below, provide a screenshot that shows the network resource has been created according to specification along with a description of what the resource does (what is its role). You may add whatever additional notes you would like. **The screenshot and description of each network component is required**. Any other notes you leave behind may make this project more useful in the future. Getting a good screenshot can be done by clicking on the resource and showing configurations in the details menu.

1. Create a VPC.
   - Tag it with "YOURLASTNAME-VPC"
   - Specify a /24 private IP address range
![](https://cdn.discordapp.com/attachments/811148913523687434/1026680396039061596/Part1_1.png)
2. Create a subnet
   - Tag it with "YOURLASTNAME-Subnet"
   - Specify a /28 private IP address range
   - Attach it to your VPC
![](https://cdn.discordapp.com/attachments/811148913523687434/1026681224628011048/Part1_2.png)
3. Create an internet gateway
   - Tag it with "YOURLASTNAME-gw"
   - Attach it to your VPC
![](https://cdn.discordapp.com/attachments/811148913523687434/1026681629218963518/Part1_3.png)
4. Create a route table
   - Tag it with "YOURLASTNAME-routetable"
   - Attach it to your VPC
   - Associate it with your subnet
   - Add a routing table rule that sends traffic to all destinations to your internet gateway
![](https://cdn.discordapp.com/attachments/811148913523687434/1026682314354335874/Part1_4.png)
5. Create a security group
   - Tag it with "YOURLASTNAME-sg"
   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses starting with 130.108)
     - Instances within the VPC
   - Attach it to your VPC
   - Image should include your Inbound rules
![](https://cdn.discordapp.com/attachments/811148913523687434/1026682929998462986/Part1_5.1.png)
![](https://cdn.discordapp.com/attachments/811148913523687434/1026682348445651064/Part1_5.png)
6. (If necessary, else skip) Create a key pair

## Part 2 - EC2 instances

1. Create a new instance. Give a write up of the following information:
   - AMI selected
     - The Amazon Machine Image (AMI) selected was ubunutu
     - default username of the instance type selected
   - Instance type selected: t2.micro
2. Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.
   - When creating an instance go under network settings and change the VPC to your specified VPC that you named. For me it was Cao-VPC.
3. Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)
   - I chose to disable auto assign. Manually assigning in my opinion is better.
   - **NOTE** - in the next few steps, you will be required to request an Elastic IP address and associate it to the instance. Factor that in to your discussion here.
4. Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.
   - 1 x 8 GiB gp2 Root volume
   - This is done through launching instance under the configure storage
5. Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it.
   - On the very top of the page after launching instance, there is a tag area you can  fill in. First will be "Name" and then "Cao-instance" for me.
6. Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.
   - Go to the tab that says security group. Fill in the information for it with a tag. For me it was Cao-sg. Once that is created click on the security group and on the top right click on the drop down arrow   and select "associate". Once that is done when you're creating the instance you can select that specific security group that is listed only if you associated it.
7. Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.
   - Under Network and Security go to Elastic IP. On the top right click allocate. Create a tag with "Name" and for me "Cao-EIP". Check mark the box of the EIP and associate Elastic IP address. 
8. Create a screenshot your instance details and add it to your project write up.
   ![instance details](https://cdn.discordapp.com/attachments/811148913523687434/1026697392877224007/Part2_8.png)
9. `ssh` in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.
   1. It is wise to copy config files you are about to change to filename.old For `/etc/hostname`, for example, I would first copy the current `hostname` file to `/etc/hostname.old`
   2. You should not change permissions on any files you are modifying. They are system config files. You may need to access them with administrative privileges.
   3. Here is a helpful resource: https://www.tecmint.com/set-hostname-permanently-in-linux/ I did not modify `/etc/hosts` on mine - do so or not as you wish.
10. Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `images` folder (optional depending on how you implement screenshots)
   - `README.md`

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project2

3. You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic IP
