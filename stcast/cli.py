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
&hfGT=R%7C
&hfC=
&hfSea=2017%7C
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


@click.command()
@click.option('--body', '-b', is_flag=True, default=False, help='Only the response body is printed')
@click.option('--min_pitches', '-m', default=1000, help='Min # of Total Pitches')
@click.argument('filename', default='result.csv', required=False)
def main(filename, body, min_pitches):
    """Statcast Http Client CLI"""

    # request params
    params = {
        'group_by': 'name',
        'hfGT': 'R|',
        'hfSea': '2017|',
        'hfZ': '1|2|3|4|5|6|7|8|9|',
        'min_abs': '0#results',
        'min_pitches': min_pitches,
        'min_results': '0',
        'player_event_sort': 'h_launch_speed',
        'player_type': 'pitcher',
        'sort_col': 'pitches',
        'sort_order': 'desc',
        'hfPT': '',
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
        'game_date_gt': '',
        'game_date_lt': '',
        'team': '',
        'position': '',
        'hfRO': '',
        'home_road': '',
        'hfFlag': '',
        'metric_1': '',
        'hfInn': ''
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