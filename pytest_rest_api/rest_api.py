"""Library for interaction with REST API"""
import requests


class RestApi:
    """Provide methods for sending requests"""

    def __init__(self, url):
        """Keep url in `self.url'.

        Intended for use with 'http://httpbin.org/' mostly, proper work with
         other API not guaranteed.

         :param url: URL ending with '/'. Requests will be sent here
         """
        self.url = url

    def get(self, headers=None):
        """
        Send GET request to URL

        :param headers: dictionary of HTTP headers, passed with GET request or None
        :return: response from server
        :rtype: requests.models.Response
        """
        if not headers:
            return requests.get('%s/get' % self.url)
        return requests.get('%s/get' % self.url, headers=headers)

    def basic_auth(self, valid_account, actual_account):
        """
        Send GET request with authentication credentials to url/:valid_user/:valid_password

        :param (str, str) valid_account: user and password - part of url, describing address where this user + password
        is valid for authentication
        :param (str, str) actual_account: user and password - credentials used for authentication attempt
        :return: response from server
        :rtype: requests.models.Response
        """
        valid_user, valid_password = valid_account
        url = '%sbasic-auth/%s/%s' % (self.url, valid_user, valid_password)
        return requests.get(url, auth=actual_account)

    def stream(self, rows):
        """
        Send GET request to url/stream/:rows to get several lines in response

        :param rows: number of rows to return
        :return: response from server
        :rtype: requests.models.Response
        """
        url = '%s/stream/%d' % (self.url, rows)
        return requests.get(url)
