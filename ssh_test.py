from paramiko import SSHClient, AutoAddPolicy

host = "192.168.0.25"
username = "lerusse"
id_rsa = RSAKey.from_private_key_file("/home/pi/.ssh/id_rsa")
# command = "xset -display :0.0 dpms force off"
command = "xset -display :0.0 q"

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(host, 22, username, id_rsa)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)

ssh.close()
