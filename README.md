# League Lobby Revealer
CLI (for now) tool to reveal people in your ranked lobby. Written in Python 3.11, inspired by [Riotphobia/LobbyReveal](https://github.com/Riotphobia/LobbyReveal).

## Examples
<details>
<summary>In Champion Select</summary>

![example1.png](examples/example1.png)
</details>

<details>
<summary>In Game (or in loading screen)</summary>

![example2.png](examples/example2.png)
<sup>dont worry i inted this game hard</sup>
</details>

## Installation

1. Download Python [here](https://www.python.org/downloads/), then clone this repo:

```commandline
git clone https://github.com/sevnnn/League-Lobby-Revealer.git
cd League-Lobby-Revealer
```

2. Next, setup your venv *(you can skip to 4. if you won't be using Python for anything else)*:

```commandline
python -m venv venv
```

3. And activate it:
```commandline
./venv/Scripts/activate
```

4. Install required packages:
```commandline
pip install -r requirements.txt
```

5. Make sure that path set in `settings.ini` is correct

## Usage

While *(having `venv` activated and)* in champion select or in game run the script:
```commandline
python main.py
```

Note that League-Lobby-Revealer is only supported on Windows.

## Roadmap

In works there is a Web UI, that would make this script work and look more like a op.gg mulitsearch, when it comes to other functionalities that are in works - head to the issues tab and [filter by the `feature` label](https://github.com/sevnnn/League-Lobby-Revealer/issues?q=is%3Aopen+is%3Aissue+label%3Afeature).

## Known Issues

- When in champion select, sometimes the script will show players that you were in party with but aren't currently. Unfortunately, cant fix that.

## Contributing

If you'd like to contribute to League-Lobby-Revealer, please create [a pull request](https://github.com/sevnnn/League-Lobby-Revealer/pulls) or open [an issue](https://github.com/sevnnn/League-Lobby-Revealer/issues). 

## License

This tool is released under the MIT License. See [LICENSE](LICENSE) file for details.

<sup>rito pls no sue</sup>
