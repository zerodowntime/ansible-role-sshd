# sshd

Ansible role to install and configure sshd

## Installation

```yaml
   ansible-galaxy install zerodowntime.awk
   ansible-galaxy install zerodowntime.selinux_python
   ansible-galaxy install zerodowntime.sshd
```

## Requirements

This role requires Ansible 2.7 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
    - name: Ubuntu
      versions:
      - bionic
      - xenial
```

## Default role variables

| Variable name                         | Required? |  Type  | Description                                                                                                          |
|:------------------------------------- |:---------:|:------:|:-------------------------------------------------------------------------------------------------------------------- |
| sshd__package_state                   |    yes    | string | installed packages state                                                                                             |
| sshd__port                            |    yes    |  int   | Specifies the port number that sshd listens on                                                                       |
| sshd__address_family                  |    yes    | string | Specifies which address family should be used by sshd                                                                |
| sshd__listen_address                  |    yes    |  list  | Specifies the local addresses sshd should listen on.                                                                 |
| sshd__hostkey                         |    yes    |  list  | Specifies a file containing a private host key used by SSH                                                           |
| sshd__permit_root_login               |    yes    | string | Specifies whether root can log in using ssh.                                                                         |
| sshd__password_authentication         |    yes    |  bool  | Specifies whether password authentication is allowed                                                                 |
| sshd__syslogfacility                  |    yes    | string | Gives the facility code that is used when logging messages                                                           |
| sshd__loglevel                        |    yes    | string | Gives the verbosity level that is used when logging messages                                                         |
| sshd__usedns                          |    yes    |  bool  | Specifies whether sshd should look up the remote host                                                                |
| sshd__x11forwarding                   |    yes    |  bool  | Specifies whether X11 forwarding is permitted.                                                                       |
| sshd__authorizedkeysfile              |    yes    | string | Specifies the file that contains the public keys that can be used for user authentication                            |
| sshd__printlastlog                    |    no     |  bool  | Specifies whether sshd should print the date and time                                                                |
| sshd__kexalgorithms                   |    yes    |  list  | Specifies the available Key Exchange algorithms                                                                      |
| sshd__ciphers                         |    yes    |  list  | Specifies the ciphers allowed for protocol version 2.                                                                |
| sshd__macs                            |    yes    |  list  | Specifies the available MAC (message authentication code) algorithms.                                                |
| sshd__authenticationmethods           |    yes    | string | Specifies the authentication methods that must be successfully completed for a user to be granted access             |
| sshd__subsystem_sftp_options          |    no     | string | Specifies Subsystem sftp options                                                                                     |
| sshd__acceptenv                       |    no     |  list  | Specifies which environment variables sent by the client will be copied to the sessions user environment.            |
| sshd__maxauthtries                    |    yes    |  int   | Specifies the maximum number of authentication attempts permitted per connection.                                    |
| sshd__maxsessions                     |    yes    |  int   | Specifies the maximum number of open shell ...                                                                       |
| sshd__pubkeyauthentication            |    yes    |  bool  | Specifies whether public key authentication is allowed                                                               |
| sshd__allowagentforwarding            |    no     |  bool  | Specifies whether ssh-agent(1) forwarding is permitted                                                               |
| sshd__printmotd                       |    yes    |  bool  | Specifies whether sshd(8) should print /etc/motd when a user logs                                                    |
| sshd__allowtcpforwarding              |    no     |  bool  | Specifies whether TCP forwarding is permitted.                                                                       |
| sshd__permittunnel                    |    yes    |  bool  | Specifies whether tun(4) device forwarding	is allowed.                                                               |
| sshd__clientaliveinterval             |    yes    |  int   | Sets a timeout interval in	seconds	after which if no data has been received from	the client                          |
| sshd__clientalivecountmax             |    yes    |  int   | Sets the number of client alive messages which may	be sent	with out sshd receiving any messages back from the client |
| sshd__gssapiauthentication            |    yes    |  bool  | Specifies whether user authentication based on GSSAPI is allowed.                                                    |
| sshd__denyusers                       |    no     |  list  | list of deny user name patterns                                                                                      |
| sshd__allowusers                      |    no     |  list  | list of allowed user name patterns                                                                                   |
| sshd__denygroups                      |    no     |  list  | list of deny groups name patterns                                                                                    |
| sshd__allowgroups                     |    no     |  list  | list of allow groups name patterns                                                                                   |
| sshd__logingracetime                  |    yes    | string | The server	disconnects after this time if the user	has not	successfully logged in                                    |
| sshd__challengeresponseauthentication |    yes    |  bool  | Specifies whether challenge-response authentication is allowed                                                       |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

| Variable name                |  Type  | Description                             |
|:---------------------------- |:------:|:--------------------------------------- |
| sshd__config                 | string | sshd config path                        |
| sshd__service_name           | string | sshd service name                       |
| sshd__moduli_file            | string | sshd moduli file path                   |
| sshd__moduli_min             |  int   | Remove small Diffie-Hellman moduli size |
| sshd__packages               |  list  | installed packages names                |
| sshd__default_syslogfacility | string | Default syslog facility                 |
| sshd__subsystem_sftp         | string | Default subsystem sftp                  |

**All static variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:
        - role: zerodowntime.sshd
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
