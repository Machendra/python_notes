import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
ssh.connect("3.90.55.22", username="ansadmin", password="admin123")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uname -a")
pip install paramiko print ssh_stdout.readlines()

'''

Login in to the server using ".pem" file:

[root@master ssh]# cat login_ssh.py
import paramiko
k = paramiko.RSAKey.from_private_key_file("/tmp/ssh/class_devops.pem")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
ssh.connect( hostname = "52.56.74.235", username = "ec2-user", pkey = k )
print "connected"
commands = [ "/sbin/ifconfig eth0","df -hT"]
for command in commands:
    print "Executing {}".format( command )
    stdin , stdout, stderr = ssh.exec_command(command)
    print stdout.read()
    print( "Errors")
    print stderr.read()
ssh.close()

'''
