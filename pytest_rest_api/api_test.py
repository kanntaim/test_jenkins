import json

import pytest
import requests

from pytest_rest_api.rest_api import RestApi


class TestApi:

    def setup(self):
        self.url = 'http://httpbin.org/'
        self.requester = RestApi(self.url)

    @pytest.fixture(params=[(('1', '1'), ('1', '1'), requests.codes['ok']),
                            (('login', 'pass'), ('login', 'pass'), requests.codes['ok']),
                            (('Логин', 'Пароль'), ('Логин', 'Пароль'), requests.codes['unauthorized']),
                            (('1', '2'), ('1', '3'), requests.codes['unauthorized']),
                            (('1', '2'), ('2', '1'), requests.codes['unauthorized']),
                            (('1', '2'), ('3', '2'), requests.codes['unauthorized']),
                            (('1' * 10000, '1' * 10000), ('1' * 10000, '1' * 10000),
                             requests.codes['request_uri_too_large'])])
    def test_auth_params(self, request):
        return request.param

    def test_auth(self, test_auth_params):
        valid_account, actual_account, expected_status_code = test_auth_params
        response = self.requester.basic_auth(valid_account, actual_account)
        assert response.status_code == expected_status_code
        if response.status_code == requests.codes['ok']:
            assert json.loads(response.text)['authenticated']
            assert json.loads(response.text)['user'] == actual_account[0] == valid_account[0]

    @pytest.mark.parametrize('headers', [{'Referer': 'http://www.myhead.org/random_page.html'},
                                         {'123': '123'}])
    def test_get(self, headers):
        response = self.requester.get(headers=headers)
        key, value = headers.popitem()
        assert response.status_code == requests.codes['ok']
        assert json.loads(response.text)['headers'][key] == value

    @pytest.mark.parametrize('params', [(0, requests.codes['ok']),
                                        (-1, requests.codes['not_found']),
                                        (1000, requests.codes['ok'])])
    def test_stream(self, params):
        rows, expected_status_code = params
        response = self.requester.stream(rows)
        assert response.status_code == expected_status_code
        if response.status_code == requests.codes['ok']:
            assert response.text.count('\n') == rows
