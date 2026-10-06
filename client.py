import socket
from shared import ECIE_commands

processor = '127.0.0.1'

def connectToController():
    PORT = 3152

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((processor, PORT))
            print(f"Connected to: {processor}, running tests...")
            s.settimeout(60.0) # to prevent terminal from crashing
            for cmd in ECIE_commands:
                while True:
                    read_data = s.recv(1024).decode('utf-8')
                    print(f"Received: {read_data}")
                    if '>>>' in read_data:
                        s.send(cmd)
                        print(f"Sent: {cmd.decode('utf-8')}")
                        break
    except Exception as e:
        print(f"Socket error: {type(e)}, {e}")

is_csdu_deployed = input("Is CSDU project deployed? (Y/n)").lower()
is_test_service_repo_running = input("Is the test services repo running? (Y/n)").lower()

acceptable_answers = ['yes', 'ye', 'y']

if (is_csdu_deployed in acceptable_answers) and (is_test_service_repo_running in acceptable_answers):
    connectToController()

while is_csdu_deployed not in acceptable_answers:
    print("Please deploy the CSDU project and try again.")
    is_csdu_deployed = input("Is CSDU project deployed? (Y/n)").lower()

while is_test_service_repo_running not in acceptable_answers:
    print("Please start the test services repo and try again.")
    is_test_service_repo_running = input("Is the test services repo running? (Y/n)").lower()