__author__ = 'tusharmakkar08'

import argparse
import json
import urllib
import webbrowser

from bs4 import BeautifulSoup
import requests


def _get_profile_id_fbv1(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']


def _get_profile_id_fbv2(username):
    """
    Input : Username
    Output : Profile Id HTML 
    """
    request_data = requests.post("http://findmyfbid.com/", data={'url': username})
    return request_data.text


def _get_user_id(html_string):
    """
    Input : HTML String from POST
    Output : Profile Id  
    """
    return BeautifulSoup(html_string, "html.parser").code.string


def _open_image_page(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with graph search results
    """
    new_url = "https://www.facebook.com/search/" + profile_id + "/photos-of"
    webbrowser.open_new_tab(new_url)


def _open_profile_pic(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with profile picture of the username
    """
    new_url = "https://graph.facebook.com/" + profile_id + "/picture?width=800"
    webbrowser.open_new_tab(new_url)


def _get_parser():
    parser = argparse.ArgumentParser(description='Tool for fetching photos from facebook')
    parser.add_argument('-u', '--username', metavar='username', type=str,
                        help='Username to analyze')
    return parser


def main(username):
    user_html = _get_profile_id_fbv2(username)
    user_id = _get_user_id(user_html)
    _open_image_page(user_id)
    _open_profile_pic(user_id)


def command_line_runner():
    parser = _get_parser()
    args = vars(parser.parse_args())

    if not args['username']:
        parser.print_help()
    else:
        main(args['username'])

    return

if __name__ == '__main__':
    command_line_runner()
