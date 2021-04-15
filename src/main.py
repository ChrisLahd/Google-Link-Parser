# Content made by ChrisLad1 (https://github.com/ChrisLad1)
# This code is not to be modified or resold by any distributor.
# LEGAL: Any third party profit made by this project can be used as a 
# legal defense / offense if neccessary.

import os
import sys
import time
import asyncio

# slow typing function meant for aesthetic pleasure.
def slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# function made asynchronous for efficiency.
async def main():
    print(os.defpath)
    # the random strings you see are color codes that make the stdout highlight certain words / chars.
    print(f'''

[\x1b[38;5;49m1\x1b[38;5;255m]: Custom
[\x1b[38;5;49m2\x1b[38;5;255m]: Preset URL queries\n''')

    # this checks to see if the main script is present in the dir of this script to make runtime work correctly.
    if "google_spider.py" not in os.listdir("modules"):        
        slow("Files are missing!.\r\n")
    else:
        try:
            slow("All Files \x1b[38;5;83mLocated!\x1b[38;5;255m")

            # this is the I/O taken from the user to determine option for scraping.
            x = input("\n\nWhich crawl settings do you want to use? --> ")
            
            options = ["1", "2"]

            # this is a validation of option for prevention of non neccesary buffer inputs.
            if x in options:
                if x == "1":
                    input("\n(NOT WORKING) Enter Keyword / Query --> ")
                
                if x == "2":
                    os.system("scrapy runspider modules/google_spider.py")

        # this is a simple check to see if a keyboard interruption occurs. If so, then it will kill the process instead of throwing tracebacks and ignored exceptions.      
        except KeyboardInterrupt:
            os.system(f'pkill -9 {os.getpid}')

asyncio.run(main())