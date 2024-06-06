#!/usr/bin/env python3
# Author: Jimmy Kolev
# A command line tool that fetches the content of a URL using HTTP GET, POST, PUT, DELETE methods

import re
import socket
import argparse
import json



def main():
    # Create the parser for the command line arguments
    parser = argparse.ArgumentParser(description="Read URL from command line and print the content of the URL") 
    # Add the arguments to the parser
    parser.add_argument('-v', '--verbose', action='store_true', help='show headers')
    parser.add_argument('-X', '--method', help='HTTP method to use (GET, POST, PUT, DELETE, etc.)')
    parser.add_argument('-H', '--header', help='HTTP header to include in the request')
    parser.add_argument('-d', '--data', help='HTTP data to include in the request')
    parser.add_argument('URL', help='URL to fetch')

    # Parse the command line arguments
    args = parser.parse_args()

    # Set the URL, method, and regex
    URL = args.URL
    method = args.method
    regex = "((((https?|ftps?|gopher|telnet|nntp)://)|(mailto:|news:))([-%()_.!~*';/?:@&=+$,A-Za-z0-9])+)"
    if not re.match(regex, URL):
        print("Invalid URL")
        return
    else:
        protocol = "HTTP"
        host = URL.split("://")[1].split("/")[0]
        port = host.split(":")[1] if ":" in host else "80"
        host_no_port = host.split(":")[0]
        path = URL.split(host)[1]
        if args.verbose:
            if method == "GET" or method is None:
                print(f"> GET {path} HTTP/1.1")
                print(f"> Host: {host_no_port}")
                print("> Accept: */*")
                print(">")
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                sock.send(f"GET {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n\r\n".encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                response_lines = headers.split("\r\n")
                for line in response_lines:
                    print(f"< {line}")
                if body.strip():  
                    try:
                        json_body = json.loads(body)
                        print("<")
                        print(json.dumps(json_body, indent=4))
                    except json.JSONDecodeError:
                        print("Error: Response body is not a valid JSON")
            if method == "DELETE":
                print(f"> DELETE {path} HTTP/1.1")
                print(f"> Host: {host_no_port}")
                print("> Accept: */*")
                print(">")
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                sock.send(f"DELETE {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n\r\n".encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                response_lines = headers.split("\r\n")
                for line in response_lines:
                    print(f"< {line}")
                if body.strip():  
                    try:
                        json_body = json.loads(body)
                        print("<")
                        print(json.dumps(json_body, indent=4))
                    except json.JSONDecodeError:
                        print("Error: Response body is not a valid JSON")
            if method == "POST":
                print(f"> POST {path} HTTP/1.1")
                print(f"> Host: {host_no_port}")
                print("> Accept: */*")
                if args.header:
                    print(f"> {args.header}")
                if args.data:
                    print(f"> Content-Length: {len(args.data)}")
                    print(f"> {args.data}")
                print(">")
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                headers = f"POST {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n"
                if args.header:
                    headers += f"{args.header}\r\n"
                if args.data:
                    headers += f"Content-Length: {len(args.data)}\r\n\r\n{args.data}"
                else:
                    headers += "\r\n"
                sock.send(headers.encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                response_lines = headers.split("\r\n")
                for line in response_lines:
                    print(f"< {line}")
                if body.strip():
                    try:
                        json_body = json.loads(body)
                        print("<")
                        print(json.dumps(json_body, indent=4))
                    except json.JSONDecodeError:
                        print("Error: Response body is not a valid JSON")   
            if method == "PUT":
                print(f"> PUT {path} HTTP/1.1")
                print(f"> Host: {host_no_port}")
                print("> Accept: */*")
                if args.header:
                    print(f"> {args.header}")
                if args.data:
                    print(f"> Content-Length: {len(args.data)}")
                    print(f"> {args.data}")
                print(">")
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                headers = f"PUT {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n"
                if args.header:
                    headers += f"{args.header}\r\n"
                if args.data:
                    headers += f"Content-Length: {len(args.data)}\r\n\r\n{args.data}"
                else:
                    headers += "\r\n"
                sock.send(headers.encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                response_lines = headers.split("\r\n")
                for line in response_lines:
                    print(f"< {line}")
                if body.strip():
                    try:
                        json_body = json.loads(body)
                        print("<")
                        print(json.dumps(json_body, indent=4))
                    except json.JSONDecodeError:
                        print("Error: Response body is not a valid JSON")
        else:
            if method == "GET" or method is None:
               sock = socket.socket()
               sock.connect((host_no_port, int(port)))
               sock.send(f"GET {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n\r\n".encode())
               response = sock.recv(1024).decode()
               headers, body = response.split("\r\n\r\n", 1)
               try:
                   json_body = json.loads(body)
                   print(json.dumps(json_body, indent=4))
               except json.JSONDecodeError:
                   print("Error: Response is not a valid JSON")
            if method == "DELETE":
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                sock.send(f"DELETE {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n\r\n".encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                try:
                     json_body = json.loads(body)
                     print(json.dumps(json_body, indent=4))
                except json.JSONDecodeError:
                     print("Error: Response is not a valid JSON")
            if method == "POST":
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                headers = f"POST {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n"
                if args.header:
                    headers += f"{args.header}\r\n"
                if args.data:
                    headers += f"Content-Length: {len(args.data)}\r\n\r\n{args.data}"
                else:
                    headers += "\r\n"
                sock.send(headers.encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                try:
                    json_body = json.loads(body)
                    print(json.dumps(json_body, indent=4))
                except json.JSONDecodeError:
                    print("Error: Response is not a valid JSON")
            if method == "PUT":
                sock = socket.socket()
                sock.connect((host_no_port, int(port)))
                headers = f"PUT {path} HTTP/1.1\r\nHost: {host_no_port}\r\nAccept: */*\r\n"
                if args.header:
                    headers += f"{args.header}\r\n"
                if args.data:
                    headers += f"Content-Length: {len(args.data)}\r\n\r\n{args.data}"
                else:
                    headers += "\r\n"
                sock.send(headers.encode())
                response = sock.recv(1024).decode()
                headers, body = response.split("\r\n\r\n", 1)
                try:
                    json_body = json.loads(body)
                    print(json.dumps(json_body, indent=4))
                except json.JSONDecodeError:
                    print("Error: Response is not a valid JSON")
            else:
                print("Invalid HTTP method")
                return
            
        
        
        
    
    
if __name__ == '__main__':
    main()

  



