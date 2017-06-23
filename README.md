# stcast

Statcast Http Client CLI For Baseball Savant

This CLI can send requests to [Baseball Savant](https://baseballsavant.mlb.com/) and You can get results as CSV.

![sample](https://user-images.githubusercontent.com/2387508/27497976-13583dbe-5898-11e7-9b6a-1e5306f9984d.jpg)

# Installation

Simply run:

```
$ pip install .
```

# Usage

To use it:

```sh
$ stcast --help
```

```
Usage: cli.py [OPTIONS]

  Statcast Http Client CLI

Options:
  -s, --season TEXT          Season. default is 2017|
  -p, --pitch_type TEXT      Picth Type:
                             FF(4-seam Fastball)
                             FT(2-seam
                             Fastball)
                             FC(Cut Fastball)
                             FS(Split-finger)
                             SI(Sinker)
                             SL(Slider)
                             CH(Changeup)
                             CU(Curveball)
                             KC(Knuckle Curve)
                             KN(Knuckleball)
                             FO(Forkball)
                             EP(Eephus)
                             SC(Screwball)
  -z, --zone TEXT            Pitch zone: Strike Zone (1 ~ 9), Ball Zone (11 ~
                             14)
  -m, --min_pitches INTEGER  Min # of Total Pitches. default is 1000
  -gt, --game_date_gt TEXT   Game Date Greater Than
  -lt, --game_date_lt TEXT   Game Date Less Than
  -hr, --home_road TEXT      Home or Road Game
  -pi, --player_id TEXT      Player ID
  -b, --body                 Only the response body is printed. default is
                             false
  --help                     Show this message and exit.
```
