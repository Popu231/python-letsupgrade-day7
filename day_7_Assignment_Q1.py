port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print("Original Dictionary:")
print(port1)

port1 = {value:key for key, value in port1.items()}
print("Dictionary after swapping:")
print(port1)