## Installation

1. Add the GitHub url to Package Control `https://github.com/pulsedemon/SublimeRemotely`
2. Search your local Package Control for `Remotely` and install

## Configuration

For this plugin to work, you need to create a map between a local directory and a remote.

Add this to your Sublime user settings file:

`"remotely_filepaths": {`
`"/Path/to/local/directory": "/usr/bin/scp $1 username@server.com:/Path/to/remote/directory$2"`
`}`

### More to come soon...