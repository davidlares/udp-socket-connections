## UDP socket connections

This is a Python script for creating deliberate UDP connections to a victim machine using network sockets for remote execution commands.

## Flags (arguments)

The program uses `argparse` module for handling CLI arguments and parsing it for custom evaluations.

Where:
  - `-l` is for listening connections
  - `-t` is for target specification (IP Address of the Victim)
  - `-p` is for the port connection

The `subprocess` module lets you connect to IO pipes and obtain return codes.

## Sockets Mode

In a Socket communication, we have a server and a client. For this script, the server (victim) acts as a **listener mode**. The client (or attacker) will set the IP address and send remote connections to the server, we can represent this role as the **sender role**

## Usage

The attack script needs to set the IP address and the port for connections:
`./remote.py -t 127.0.0.1 -p 9999`

The "victim" should run this script on the same port that the attacker used:
`./remote.py -l -p 9999`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
