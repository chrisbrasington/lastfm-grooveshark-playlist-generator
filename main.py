##import sys
import pylast
import pygrooveshark
from keys import lastfm

LASTFM_NETWORK = ''
GROOVESHARK_NETWORK = ''

def init():
    global LASTFM_NETWORK
    global GROOVESHARK_NETWORK
    LASTFM_NETWORK = pylast.LastFMNetwork(api_key=lastfm.key, api_secret=lastfm.secret, username=lastfm.username,
                                          password_hash=pylast.md5(lastfm.password))
    GROOVESHARK_NETWORK = pygrooveshark.GrooveSharkNetwork()


if __name__ == '__main__':
    init()

    raylinth = pylast.User('raylinth', LASTFM_NETWORK)
    print 'lastfm user: ', raylinth.name

    recenttrack = raylinth.get_recent_tracks(1)[0].track
    artist = recenttrack.get_artist().name

    print 'last artist: ', artist

    groovedata = GROOVESHARK_NETWORK.get_song_search_results(artist, limit=1)
    print '\ngrooveshark song search: \n\n', groovedata