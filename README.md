# stcast

Statcast Http Client CLI


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ stcast --help

```
Usage: cli.py [OPTIONS] [FILENAME]

  Statcast Http Client CLI

Options:
  -s, --season TEXT          Season. default is 2017|
  -p, --pitch_type TEXT      Picth Type:
                             FF 4-seam Fastball
                             FT 2-seam Fastball
                             FC Cut Fastball
                             FS Split-finger
                             SI Sinker
                             SL
                             Slider
                             CH Changeup
                             CU Curveball
                             KC Knuckle Curve
                             KN Knuckleball
                             FO Forkball
                             EP Eephus
                             SC Screwball
  -z, --zone TEXT            Pitch zone: Strike Zone (1 ~ 9), Ball Zone (11 ~
                             14)
  -m, --min_pitches INTEGER  Min # of Total Pitches. default is 1000
  -gt, --game_date_gt TEXT   Game Date Greater Than
  -lt, --game_date_lt TEXT   Game Date Less Than
  -hr, --home_road TEXT      Home or Road Game
  -pi, --player_id TEXT      Player ID
  -b, --body                 Only the response body is printed. default is
                             true
  --help                     Show this message and exit.
```
