- HTTP Status Codes reference
https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html

- Host Ports basics
https://en.wikipedia.org/wiki/Port_(computer_networking)

- Small socket example using netcat
-- Terminal 1
netcat -l <port number>
Example: netcat -l 8000

-- Terminal 2
# Created a file
echo "Hello Sindu" > send_file
netcat 127.0.0.1 8000 < send_file


- Small socket example using netcat and host/IP
-- Terminal 1
# -k in netcat indicates for us to listen on the host and port continuesly
netcat -k -l <IP/Host> <port number>
Example: netcat -k -l 192.168.0.6 8000

-- Terminal 2
# Created a file
echo "Hello Sindu" > send_file
netcat <IP/Host> 8000 < send_file
netcat 192.168.0.6 8000 < send_file

