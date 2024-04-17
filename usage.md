# `org-todo-send`

Sends a message to recipients with their TODOs from an Org file. The TODO nodes in the Org file should be tagged with the recipient's name. Ex: @alice

**Usage**:

```console
$ org-todo-send [OPTIONS] ORG_FILE SENDER RECIPIENTS_FILE [API_URL]
```

**Arguments**:

* `ORG_FILE`: Path to your Org file  [required]
* `SENDER`: The Signal phone number you are sending from.  [env var: SIGNAL_SENDER;required]
* `RECIPIENTS_FILE`: Path to a TOML file containing phone numbers or IDs of recipients.  [required]
* `[API_URL]`: URL of your Signal REST API.  [env var: SIGNAL_API;default: http://localhost:8080]

**Options**:

* `--message-title TEXT`: Title of the message  [default: TODOs]
* `--html / --no-html`: Attach an HTML export of the Org file in the message.  [default: no-html]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
