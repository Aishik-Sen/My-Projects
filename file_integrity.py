import argparse,hashlib,sys
from colorama import Fore,init
init()

##function to calculate SHA-256 hash
def calculate_hash(file_path):
    sha256_hash=hashlib.sha256()
    ##open file in binary mode for reading
    with open(file_path,"rb")as file:
        ##read in 64KB blocks
        while True:
            data=file.read(65536)
            if not data:
                break
            sha256_hash.update(data)##update the hash
    ##return hex representation of hash
    return sha256_hash.hexdigest()

def verify_hash(downloaded_file,expected_hash):
    calculated_hash=calculate_hash(downloaded_file)
    ##calculate the hasha nd compare with expected value
    return calculated_hash==expected_hash

##Take user inputs for 
parser=argparse.ArgumentParser(description="Verify file integrity by checking hash of a downloaded software file")
## Define 2 CLI arguments:
## -f or --file: Path to the downloaded software file 
## --hash: Expected hash value
parser.add_argument("-f","--file",dest="downloaded_file",required=True,help="Path to the downloaded software file")
parser.add_argument("--hash",dest="expected_hash",required=True,help="Expected hash value")
##parse the CLI arguments when running 
args=parser.parse_args()
##Check if all arguments were provided
if not args.downloaded_file or not args.expected_hash:
    print(Fore.RED+"[!] Please specify file and hash")
    sys.exit()

##check the hash verification
if verify_hash(args.downloaded_file,args.expected_hash):
    print(f"{Fore.GREEN}[+] Hash verification successful. The software is authentic")
else:
    print(f"{Fore.RED}[!] Hash verification failed. The software is not authentic and/or has been tampered with")

