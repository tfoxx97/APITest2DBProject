#! python 3.14.6
"""
Server for the ECIE test suite.

* Handles a single client at a time (for the demo – production‑grade code
  would need threading/asyncio, connection pooling, etc.)
* Sends the test result back to the client.
* Persists the result in a SQLite database whose schema is defined in
  ``databaseAPI.py``.
"""

import socket
import uuid
import random
from datetime import datetime
from databaseAPI import SessionLocal, get_or_create_firmware, write_test_result
from shared import ECIE_commands, firmware_str, component, feature

# --------------------------------------------------------------------------- #
#  Socket / Protocol constants
# --------------------------------------------------------------------------- #

GET_INFO_MSG = ECIE_commands[0]
PORT = 3152
SERVER = "127.0.0.1"      # control processor where we RX data from
ADDR = (SERVER, PORT)

# --------------------------------------------------------------------------- #
#  Server
# --------------------------------------------------------------------------- #
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(scenarios: list[bytes]):
    """
    Main event loop – one connection at a time.

    The flow mirrors the original code:
    1.  Accept a connection.
    2.  Wait for the first command (`GET_INFO_MSG`) and reply with
        firmware/component/feature information.
    3.  For each subsequent command, generate a pass/fail,
        send the result back to the client **and** write it to the DB.
    """
    with server_socket:
        server_socket.bind(ADDR)
        server_socket.listen()
        print(f"Server listening on {SERVER}:{PORT}")

        while True:                               # keep the server alive
            conn, addr = server_socket.accept()
            with conn:
                conn.send(b">>>")                 # hand‑shake prompt
                print(f"Connected by {addr}")

                # ---------- 1) Gather system info  ----------
                # Client will first send GET_INFO_MSG
                data = conn.recv(1024)
                if data != GET_INFO_MSG:
                    print("Unexpected first command – closing")
                    continue
                
                date_tested = datetime.now()

                conn.send(
                    f"firmware: {firmware_str}\r\n"
                    f"{component}\r\n"
                    f"{feature}\r\n"
                    f"datetime: {date_tested}\r\n"
                    ">>>\r\n"
                    .encode("utf-8")
                )

                # ---------- 2) Handle each test scenario ----------
                with SessionLocal() as session:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break

                        # A scenario finished – write result to DB
                        if data == scenarios[-1]:
                            # last command – nothing more to do
                            break

                        # --------------------------------------------------
                        # Scenario handling
                        # --------------------------------------------------
                        if data in scenarios[1:]:
                            # Create a deterministic integer ID from a UUID
                            scenario_uuid = uuid.uuid4()
                            scenario_id = scenario_uuid.int % (1 << 31)

                            # Random pass / fail
                            pass_fail = random.choice(["pass", "fail"])
                            result_bool = pass_fail == "pass"
                            debug_msg = None

                            if not result_bool:
                                debug_msg = {"teardown": "Reason for failure: ..."}

                            # Send result back to the client
                            conn.send(
                                f"scenario ID={scenario_id}\r\n"
                                f"Result: {pass_fail}\r\n"
                                f"{debug_msg or 'None'}\r\n"
                                ">>>\r\n".encode("utf-8")
                            )

                            # Persist to the DB
                            write_test_result(
                                session,
                                firmware_str,
                                date_tested,
                                component,
                                feature,
                                scenario_id,
                                result_bool,
                                debug_msg,
                            )

if __name__ == "__main__":
    handle_client(ECIE_commands)