# mqttdecode

This is a tool that attempts to convert hex strings representing MQTT packets
into a human readable form.

It handles multiple packets at once, displays results for different protocol
versions, and highlights most protocol errors and malformed packets.

## Running

mqttdecode can run with hex strings provided as command arguments, as input
from stdin, or as input from a file. Command line inputs are concatenated
together to make a single line, then decoded. File and stdin data is treated as
individual lines.

Command line arguments:
```
mqttdecode 50020001
```

Stdin:
```
echo 50020001 | mqttdecode
```

File:
```
mqttdecode -f hexstrings.txt
```

If multiple input options are used, they are processed in the order: stdin,
file, arguments.

## Options

```
usage: mqttdecoder [-h] [-s {4,5}] [--colour | --no-colour] [--no-separator] [-f FILE] [hex ...]
```

### Specification version

By default, mqttdecode will attempt to process hex string into MQTT v3.1.1 and
v5.0 packets, with the exception of for CONNECT packets where the packet itself
determines which protocol specification to use. Often it is clear which
protocol specification is the correct one, because errors will occur in the
other case.

If you wish to restrict decoding to a given protocol spec, use the
`--force-spec`, or `-s` option. This must be given the argument `4` or `5`, for
MQTT v3.1.1 or v5.0 respectively.

```
mqttdecode -s 4 f00100
mqttdecode -s 5 f00100
```

### Coloured output

By default, mqttdecode will use ANSI colour codes to highlight different parts
of the packet to make it easier to understand, if the output is a TTY and will
not use colour if the output is not a TTY. If you want to override this
behaviour, use `--colour` or `--no-colour`.

Colour output is not available on Windows.

```
mqttdecode --no-colour f00100
```

### Packet separator

By default, mqttdecode will print a separator line (------------) between
multiple packets decoded in the same run. This is helpful if both v3.1.1 and
v5.0 decoded versions of each packet are being printed. If you are using `-s 4`
or `-s 5`, you may wish to suppress the separator using `--no-separator`.


## Example Output

Command:
```
mqttdecode 0000 \
           102000044d51545404c2003c00000008757365726e616d65000870617373776f7264 \
           20020000 \
           3015000c746f7069632d66696c7465726d657373616765 \
           40020001 \
           50020001 \
           62020001 \
           70020001 \
           82110001000c746f7069632d66696c74657201 \
           9003000101 \
           a2100002000c746f7069632d66696c746572 \
           b0020002 \
           c000 \
           d000 \
           e000 \
           f00100
```


Output:
```
Hex:               00 00
Command:           RESERVED
Length:            0

------------------------------

Hex:               10 20 0004 4d515454 04 c2 003c 0000 0008 757365726e616d65 0008 70617373776f7264
Command:           CONNECT v3.1.1
Length:            32
Clean session:     True
Keepalive:         60
Client ID:         (length: 0)
Username:          (length: 8) username
Password:          (length: 8) password

------------------------------

Hex:               20 02 00 00
Command:           CONNACK v3.1.1
Length:            2
Session present:   False
Return code:       0 (accepted)

Hex:               20 02 00 00
Command:           CONNACK v5.0
Length:            2
Session present:   False
Reason code:       0 (success)

------------------------------

Hex:               30 15 000c 746f7069632d66696c746572 6d657373616765
Command:           PUBLISH v3.1.1
QoS:               0
Flags:             no-retain
Length:            21
Topic:             (length: 12) topic-filter
Payload:           (length: 7) message

Hex:               00 15 000c 746f7069632d66696c746572 6d 657373616765
Command:           PUBLISH v5.0
QoS:               0
Flags:             no-retain
Length:            21
Topic:             (length: 12) topic-filter
Properties Length: 109 > remaining length
Payload:           (length: 6) essage

------------------------------

Hex:               40 02 0001
Command:           PUBACK v3.1.1
Length:            2
Packet ID:         1

Hex:               40 02 0001
Command:           PUBACK v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

Hex:               50 02 0001
Command:           PUBREC v3.1.1
Length:            2
Packet ID:         1

Hex:               50 02 0001
Command:           PUBREC v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

Hex:               62 02 0001
Command:           PUBREL v3.1.1
Fixed header:      0x62
Length:            2
Packet ID:         1

Hex:               62 02 0001
Command:           PUBREL v5.0
Fixed header:      0x62
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

Hex:               70 02 0001
Command:           PUBCOMP v3.1.1
Length:            2
Packet ID:         1

Hex:               70 02 0001
Command:           PUBCOMP v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

Hex:               82 11 0001 000c 746f7069632d66696c746572 01
Command:           SUBSCRIBE v3.1.1
Length:            17
Packet ID:         1
Topic:             (length: 12) topic-filter
  QoS:             1

Hex:               82 11 0001 00 0c74 6f7069632d66696c74657201
Command:           SUBSCRIBE v5.0
Length:            17
Packet ID:         1
Properties Length: 0
Topic:             (length: 3188) opic-filter?
  Flags:           Subscription options malformed: ?

------------------------------

Hex:               90 03 0001 01
Command:           SUBACK v3.1.1
Length:            3
Packet ID:         1
Granted QoS:       1

Hex:               90 03 0001 01
Command:           SUBACK v5.0
Length:            3
Packet ID:         1
Properties Length: 1 > remaining length

------------------------------

Hex:               a2 10 0002 000c 746f7069632d66696c746572
Command:           UNSUBSCRIBE v3.1.1
Length:            16
Packet ID:         2
Topic:             (length: 12) topic-filter

Hex:               a2 10 0002 00 0c74 6f7069632d66696c746572
Command:           UNSUBSCRIBE v5.0
Length:            16
Packet ID:         2
Properties Length: 0
Topic:             (length: 3188) opic-filter?

------------------------------

Hex:               b0 02 0002
Command:           UNSUBACK v3.1.1
Length:            2
Packet ID:         2

Hex:               b0 02 0002
Command:           UNSUBACK v5.0
Length:            2
Packet ID:         2

------------------------------

Hex:               c0 00
Command:           PINGREQ v3.1.1/v5.0
Length:            0

------------------------------

Hex:               d0 00
Command:           PINGRESP v3.1.1/v5.0
Length:            0

------------------------------

Hex:               e0 00
Command:           DISCONNECT v3.1.1
Length:            0

Hex:               e0 00
Command:           DISCONNECT v5.0
Length:            0
Reason code:       ? (Invalid reason code)

------------------------------

Hex:               f0 01 00
Command:           AUTH
Length:            1
Excess bytes:      00

Hex:               f0 01 00
Command:           AUTH v5.0
Length:            1
Reason code:       0 (success)
```
