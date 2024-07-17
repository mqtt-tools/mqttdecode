# mqttdecode

This is a tool that attempts to convert hex strings representing MQTT packets
into a human readable form.

It handles multiple packets at once, displays results for different protocol
versions, and highlights most protocol errors and malformed packets.

## Example


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
RESERVED
Length:            0

------------------------------

CONNECT v3.1.1
Length:            32
Clean session:     True
Keepalive:         60
Client ID:
Username:          username
Password:          password

------------------------------

CONNACK v3.1.1
Length:            2
Session present:   False
Return code:       0 (accepted)

CONNACK v5.0
Length:            2
Session present:   False
Reason code:       0 (success)

------------------------------

PUBLISH v3.1.1
Length:            21
Topic:             topic-filter
QoS:               0
Flags:             no-retain
Payload:           message

PUBLISH v5.0
Length:            21
Topic:             topic-filter
QoS:               0
Flags:             no-retain
Properties Length: 109 > remaining length
Payload:           essage

------------------------------

PUBACK v3.1.1
Length:            2
Packet ID:         1

PUBACK v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

PUBREC v3.1.1
Length:            2
Packet ID:         1

PUBREC v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

PUBREL v3.1.1
Length:            2
Packet ID:         1

PUBREL v5.0
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

PUBCOMP v3.1.1
Length:            2
Packet ID:         1

PUBCOMP v5.0
Length:            2
Packet ID:         1
Length:            2
Packet ID:         1
Reason code:       ? (Invalid reason code)

------------------------------

SUBSCRIBE v3.1.1
Length:            17
Packet ID:         1
Topic:             topic-filter
  QoS:             1

SUBSCRIBE v5.0
Length:            17
Packet ID:         1
Properties Length: 0
Topic:             opic-filter
  Flags:           Subscription options malformed: ?

------------------------------

SUBACK v3.1.1
Length:            3
Packet ID:         1
Granted QoS:       1

SUBACK v5.0
Length:            3
Packet ID:         1
Properties Length: 1 > remaining length

------------------------------

UNSUBSCRIBE v3.1.1
Length:            16
Packet ID:         2
Topic:             topic-filter

UNSUBSCRIBE v5.0
Length:            16
Packet ID:         2
Properties Length: 0
Topic:             opic-filter

------------------------------

UNSUBACK v3.1.1
Length:            2
Packet ID:         2

UNSUBACK v5.0
Length:            2
Packet ID:         2

------------------------------

PINGREQ v3.1.1/v5.0
Length:            0

------------------------------

PINGRESP v3.1.1/v5.0
Length:            0

------------------------------

DISCONNECT v3.1.1
Length:            0

DISCONNECT v5.0
Length:            0
Reason code:       ? (Invalid reason code)

------------------------------

AUTH v5.0
Length:            1
Reason code:       0 (success)
```
