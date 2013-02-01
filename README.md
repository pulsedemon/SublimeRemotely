![remotely logo](https://raw.github.com/pulsedemon/SublimeRemotely/7f5b52099e94fe63336804c79c3fff6b02165445/remotely.png)

Keep local files in sync with a remote copy

##Requirements
1. Linux or OSX
2. Sublime

## Installation

1. Add the GitHub url to Package Control `https://github.com/pulsedemon/SublimeRemotely`
2. Search your local Package Control for `Remotely` and install

## Configuration

For this plugin to work, you need to create a map between a local directory and a remote.

Add this to your Sublime user settings file:

```js
"remotely_filepaths": {
  "/Path/to/local/directory": "/usr/bin/scp $1 username@server.com:/Path/to/remote/directory$2"
}
```

Feel free to change the file transfer protocol.

####More to come soon…####
