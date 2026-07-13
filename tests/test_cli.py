import subprocess

import runs


def run_mqttdecode(arguments):
    """
    Utility function to invoke `mqttdecode`.

    :param arguments:
    :return:
    """
    command = f"python mqttdecode {arguments}"
    response = runs.run(command)
    return response


def test_cli_version(capfd):
    """
    Verify `mqttdecode --version` succeeds.
    """
    run_mqttdecode("--version")
    out, err = capfd.readouterr()
    assert out.strip() == "mqttdecode version 0.0.1"


def test_cli_mqttdecode(capfd):
    """
    Verify basic `mqttdecode` incantation.
    """
    output = subprocess.check_output(["python", "mqttdecode", "50020001"])
    assert output == b"""
Hex:               50 02 0001
Command:           PUBREC v3.1.1
Length:            2
Packet ID:         1

Hex:               50 02 0001
Command:           PUBREC v5.0
Length:            2
Packet ID:         1
Reason code:       0 (success)

""".lstrip()
