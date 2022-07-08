from datetime import datetime

end_time = datetime(2022, 7, 9, 12)

sites_to_block = ['www.traleor.com','traleor']
 # in Windows, each site routing occurs in a file called hosts 
 # Thus whenever we wish to have access to a specified file, our computers checks the routing in this file and redirects us to the site we wish to have access to.
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# The 'r' used means we want to use the path specified as a raw string
# Since we are using back slashes, we don't want the interpreter to see it as aspecial character but see it as the path that it is.

redirect = "127.0.0.1"

# Function to block sites
def block_sites():
    #we compare the currend time to the end_time defined above
    if datetime.now() < end_time:
        print("Blocking Sites")
        # the process of blocking the specified sites consists of opening the hosts files, "rerouting" the sites to be blocked to our local host
        # or any other site we want
        with open(hosts_path, 'r+') as hostsfile:  #Here we are opening the hosts file in read and write mode
            hosts_content = hostsfile.read()
            for site in sites_to_block:  # for all elements in our sites_to_block array
                if site not in hosts_content: # we first check if the site to be blocked is not already in the file
                    hostsfile.write(redirect + " " + site + "\n") # if it is not, we write this site along with its redirect url
    
    # Now we specify what happens if we are no longer below the end_time specified
    # In essence, if we are above the range, we should have access to the sites blocked
    # We do tjis by removing the redirect path that we specified in the hosts file

    else:
        print("Unblocking Sites")
        with open(hosts_path, 'r+') as hostfile:
            # Once we open the hosts file, we iterate over every line to check for the sites we blocked.
            # When we get to the site string, we remove it and thus granting back access to the site
            lines = hostfile.readlines() # loading all files in hostsfiles in the variable line
            # we proceed by setting the pointer to the very beginning of the file
            hostsfile.seek(0)

            #we iterate over all the lines to check fot the sites we blocked
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostfile.truncate() #we truncate the remaining entries in the file once we see the site string

# since we're are done with the block_sites function, we run it
if __name__ == "__main__":
    block_sites()

