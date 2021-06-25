import paramiko
import datetime

output_file_name = "status.html"
today = (datetime.datetime.now())
now = today.strftime("%m/%d/%Y %H:%M:%S")

Name1 = " Premium | SG | 01 "
hostname1 = "174.138.27.160"
port1 = 22
user1 = "lahiru"
passw1 = "lahiru1998"

Name2 = " Premium | SG | 02 "
hostname2 = "192.46.225.158"
port2 = 22
user2 = "lahiru"
passw2 = "lahiru1998"

Name3 = " Free | Download | SG "
hostname3 = "68.183.178.31"
port3 = 22
user3 = "free"
passw3 = "free"

Name4 = " Free | Download | JP "
hostname4 = "103.29.68.180"
port4 = 22
user4 = "free1"
passw4 = "free"

Name5 = " Free | Download | FR "
hostname5 = "46.101.101.176"
port5 = 22
user5 = "free"
passw5 = "free"

Name6 = " Free | Download | CA "
hostname6 = "134.122.33.150"
port6 = 22
user6 = "free"
passw6 = "free"

Name7 = " Torrent | Download | SG  "
hostname7 = "torrent-3.sshstores.net"
port7 = 997
user7 = "free"
passw7 = "free"

Name8 = " Torrent | Download | FR  "
hostname8 = "torrent-2.sshstores.net"
port8 = 997
user8 = "free"
passw8 = "free"

# floats needed to determine accurate percentage
servers_up = 0.00
servers_down = 0.00
servers_percent = 0.00

# test server 1
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname1, port=port1, username=user1, password=passw1)

except paramiko.AuthenticationException:
    server1down = 1
    servers_down += 1
    server1up = 0
else:
    server1up = 1
    servers_up += 1

# test server 2
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname2, port=port2, username=user2, password=passw2)

except paramiko.AuthenticationException:
    server2down = 1
    servers_down += 1
    server2up = 0
else:
    server2up = 1
    servers_up += 1

# test server 3

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname3, port=port3, username=user3, password=passw3)

except paramiko.AuthenticationException:
    server3down = 1
    servers_down += 1
    server3up = 0
else:
    server3up = 1
    servers_up += 1


# test server 4

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname4, port=port4, username=user4, password=passw4)

except paramiko.AuthenticationException:
    server4down = 1
    servers_down += 1
    server4up = 0
else:
    server4up = 1
    servers_up += 1

# test server 5

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname5, port=port5, username=user5, password=passw5)

except paramiko.AuthenticationException:
    server5down = 1
    servers_down += 1
    server5up = 0
else:
    server5up = 1
    servers_up += 1

# test server 6

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname6, port=port6, username=user6, password=passw6)

except paramiko.AuthenticationException:
    server6down = 1
    servers_down += 1
    server6up = 0
else:
    server6up = 1
    servers_up += 1

# test server 7

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname7, port=port7, username=user7, password=passw7)

except paramiko.AuthenticationException:
    server7down = 1
    servers_down += 1
    server7up = 0
else:
    server7up = 1
    servers_up += 1

# test server 7

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname8, port=port8, username=user8, password=passw8)

except paramiko.AuthenticationException:
    server8down = 1
    servers_down += 1
    server8up = 0
else:
    server8up = 1
    servers_up += 1

# determine percentage of servers that are online
server_total = (servers_up + servers_down)
servers_percent = ((server_total - servers_down) / server_total)
servers_percent = round(servers_percent, 2)
servers_percent = str(servers_percent)

# begin writing the file
html_file = open(output_file_name, 'w', buffering=1)
html_file.write("<html>")
html_file.write("\n")
html_file.write("<head>")
html_file.write("\n")
html_file.write("<link rel=\"stylesheet\" href=\"css/styles.css\">")
html_file.write("\n")
html_file.write("<script type=\"text/javascript\" src=\"js/jquery.min.js\"></script>")
html_file.write("\n")
html_file.write("<script type=\"text/javascript\" src=\"js/circle-progress.js\"></script>")
html_file.write("\n")
html_file.write("<script type=\"text/javascript\" src=\"js/jquery.noty.packaged.min.js\"></script>")
html_file.write("\n")
html_file.write("</head>")
html_file.write("\n")
html_file.write("<body>")
html_file.write("\n")
html_file.write("<div id=\"circle\"><strong></strong></div>")
html_file.write("\n")
html_file.write("<script>")
html_file.write("\n")
html_file.write("$(\'#circle\').circleProgress({")
html_file.write("\n")
html_file.write("value: " + servers_percent + ",")
html_file.write("\n")
html_file.write("size: 200,")
html_file.write("\n")
html_file.write("thickness: 20,")
html_file.write("\n")
html_file.write("emptyFill: \"#262b33\",")
html_file.write("\n")
html_file.write("fill: { color: [\"#0277BD\"]}")
html_file.write("\n")
html_file.write(
    "}).on(\'circle-animation-progress\', function(event, progress, stepValue) {$(this).children(\'strong\').text(("
    "stepValue * 100).toFixed(0) + \'%\');});")
html_file.write("\n")
html_file.write("</script>")
html_file.write("\n")
html_file.write("<script type=\"text/javascript\" src=\"js/notifications.js\"></script>")
html_file.write("\n")
html_file.write("<script>noty({text: \"Report created " + now + "\" ,type: \'information\'});</script>")
html_file.write("\n")
html_file.write("<body>")
html_file.write("\n")
html_file.write("<div class=\"table-title\">")
html_file.write("\n")
html_file.write("<h3> </h3>")
html_file.write("\n")
html_file.write("</div>")
html_file.write("\n")
html_file.write("<table class=\"table-fill\">")
html_file.write("\n")
html_file.write("<thead>")
html_file.write("\n")
html_file.write("<tr>")
html_file.write("\n")
html_file.write("<th class=\"text-left\">Server</th>")
html_file.write("\n")
html_file.write("<th class=\"text-left\">Status</th>")
html_file.write("\n")
html_file.write("</tr>")
html_file.write("\n")
html_file.write("</thead>")
html_file.write("\n")
html_file.write("<tbody class=\"table-hover\">")

# main code for bot

# server 1 table
if server1up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name1 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name1 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 2 table
if server2up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name2 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name2 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 3 table


if server3up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name3 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name3 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 4 table


if server4up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name4 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name4 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 5 table


if server5up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name5 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name5 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 6 table


if server6up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name6 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name6 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 7 table


if server7up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name7 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name7 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")

# server 8 table


if server8up == 1:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name8 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"green\">Online</td>")
    html_file.write("\n")
    html_file.write("</tr>")
else:
    html_file.write("<tr>")
    html_file.write("\n")
    html_file.write("<td class=\"text-left\">" + Name8 + "</td>")
    html_file.write("\n")
    html_file.write("<td class=\"red\">Offline</td>")
    html_file.write("\n")
    html_file.write("</tr>")


html_file.write("\n")
html_file.write("</tbody>")
html_file.write("\n")
html_file.write("</table>")
html_file.write("\n")
html_file.write("</body>")
html_file.write("\n")
html_file.write("</html>")
html_file.close()
