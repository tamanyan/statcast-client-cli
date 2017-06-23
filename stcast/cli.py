import click
import os
import sys
import urllib.request, urllib.parse
import socket
socket.setdefaulttimeout(30)

BASE_URL = 'https://baseballsavant.mlb.com/statcast_search/csv'

"""
https://baseballsavant.mlb.com/statcast_search
?hfPT=
&hfAB=
&hfBBT=
&hfPR=
&hfZ=
&stadium=
&hfBBL=
&hfNewZones=
&hfGT=R|
&hfC=
&hfSea=2017|
&hfSit=
&player_type=pitcher
&hfOuts=
&opponent=
&pitcher_throws=
&batter_stands=
&hfSA=
&game_date_gt=
&game_date_lt=
&team=
&position=
&hfRO=
&home_road=
&hfFlag=
&metric_1=
&hfInn=
&min_pitches=0
&min_results=0
&group_by=name
&sort_col=pitches
&player_event_sort=h_launch_speed
&sort_order=desc
&min_abs=0#
"""

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

help_pitch_type = """Picth Type:
FF(4-seam Fastball)
FT(2-seam Fastball)
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
"""

@click.command()
@click.option('--season', '-s', default='2017|', help='Season. default is 2017|')
@click.option('--pitch_type', '-p', default='', help=help_pitch_type)
@click.option('--zone', '-z', default='', help='Pitch zone: Strike Zone (1 ~ 9), Ball Zone (11 ~ 14)')
@click.option('--min_pitches', '-m', default=1000, help='Min # of Total Pitches. default is 1000')
@click.option('--game_date_gt', '-gt', default='', help='Game Date Greater Than')
@click.option('--game_date_lt', '-lt', default='', help='Game Date Less Than')
@click.option('--home_road', '-hr', default='', help='Home or Road Game')
@click.option('--player_id', '-pi', default='', help='Player ID')
@click.option('--body', '-b', is_flag=True, default=False, help='Only the response body is printed. default is false')
def main(season, pitch_type, zone, min_pitches, game_date_gt, game_date_lt, home_road, player_id, body):
    """Statcast Http Client CLI"""

    # request params
    params = {
        'group_by': 'name',
        'hfGT': 'R|L',
        'hfSea': season,
        'hfZ': zone,
        'min_abs': '0#results',
        'min_pitches': min_pitches,
        'min_results': '0',
        'player_event_sort': 'h_launch_speed',
        'player_type': 'pitcher',
        'sort_col': 'pitches',
        'sort_order': 'desc',
        'hfPT': pitch_type,
        'hfAB': '',
        'hfBBT': '',
        'hfPR': '',
        'stadium': '',
        'hfBBL': '',
        'hfNewZones': '',
        'hfC': '',
        'hfSit': '',
        'hfOuts': '',
        'opponent': '',
        'pitcher_throws': '',
        'batter_stands': '',
        'hfSA': '',
        'game_date_gt': game_date_gt,
        'game_date_lt': game_date_lt,
        'team': '',
        'position': '',
        'hfRO': '',
        'home_road': home_road,
        'hfFlag': '',
        'metric_1': '',
        'hfInn': '',
        'type': 'detail' if len(player_id) > 0 else '',
        'player_id': player_id
    }

    # request url
    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    # request
    req = urllib.request.Request(url, headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Stcast/1.0.0-dev',
        'Connection': 'keep-alive',
        'Host': 'baseballsavant.mlb.com'
    })

    if not body:
        click.secho('GET: ', fg='red', nl=False)
        click.secho(url + '\n', blink=True, bold=True)

        # print headers
        click.secho('Request Headers', blink=True, bold=True)
        for key, val in req.headers.items():
            click.echo(key + ': ', nl=False)
            click.secho(val, fg='green')
        click.echo('')

    with urllib.request.urlopen(req, timeout=30) as res:
        if not body:
            # print headers
            click.secho('Response Headers', blink=True, bold=True)
            for key, val in res.headers.items():
                click.echo(key + ': ', nl=False)
                click.secho(val, fg='green')
            click.echo('')

        # print result
        csv = res.read().decode("utf-8")
        click.echo(csv)


if __name__ == '__main__':
    main()