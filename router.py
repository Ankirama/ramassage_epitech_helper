import hmac, datetime, base64, re, requests, json, pytz

class Router(object):
    """
    This class will be our router and will be used as a parent class to give function to communicate with API
    This is an helper class

    :todo: Add log ?
    """

    DEFAULT_BASE_URL = "api.ramassage.epitech.eu"
    DEFAULT_API_VERSION = "1.0"
    REGEX_PARAM_URI = ":[a-z_]+"
    REQUEST_TYPE = {
        'put': requests.put,
        'post' : requests.post,
        'patch': requests.patch,
        'get': requests.get,
        'delete': requests.delete
    }

    def __init__(self, tz="Europe/Paris"):
        """
        Constructor class, it will set uuid / secret (from config.py file) and timezone
        :param tz: Timezone used for datetime
        :type tz: str
        """
        try:
            with open('settings.json') as f:
                config = json.load(f)
        except FileNotFoundError as e:
            print("You must create a settings.json file with UUID / SECRET")
            exit(1)
        else:
            self.uuid = config['UUID']
            self.secret = bytearray(config['SECRET'], "utf-8")
            self.tz = pytz.timezone(tz)


    def request(self, route, body, *args):
        """
        Function used to execute a request (get, post, ....) from a child class
        It will generate URL and headers and it will use requests lib to execute it

        :param route: Refer to key in self.ROUTES from child class
        :param body: Used for post / put / patch request type
        :param args: example: /:id/:toto with param1, param2 will become /param1, param2
        :type route: str
        :type body: dict
        :type args: tuple
        :return: Return dict with "error", "status_code" and "content". If any error (500 / 4XX) then error = True
        :rtype: dict
        :todo: clean code + split it maybe
        """
        if (not route in self.ROUTES):
            raise ValueError('Unknown ROUTE: [%s]' % route)
        if (not self.ROUTES[route]['method'] in self.REQUEST_TYPE):
            raise ValueError('Unknown method: [%s]' % self.ROUTES[route]['method'])
        arg = list(args)
        method = self.ROUTES[route]['method']
        path = re.sub(self.REGEX_PARAM_URI, lambda _ : str(arg.pop(0)), self.ROUTES[route]['path'], len(args))
        resource = self.__class__.__name__.lower()
        url = "http://%s/%s/%s%s" % (self.DEFAULT_BASE_URL, self.DEFAULT_API_VERSION, resource, path)
        req_function = self.REQUEST_TYPE[method]
        if (method != "get"):
            body_json = json.dumps(body)
        else:
            body_json = {}
        if method == "post":
            if (body == {}):
                data = ""
            else:
                data = body_json
        else:
            data = "/%s/%s%s" % (self.DEFAULT_API_VERSION, resource, path)
        headers = self._headers(data)
        r = req_function(url, headers=headers, data=body_json)
        if r.status_code == 200:
            return {'error': False, 'status_code': r.status_code, 'content': r.json()}
        else:
            return {'error': True, 'status_code': r.status_code, 'content': r.content}


    def _headers(self, data):
        """
        Create custom header for every request
        It will generate Date, Authorization and Content-Type

        :param data: data used to create authorization value
        :type data: str
        :return: headers generated with Date / Authorization / Content-Type
        :rtype: dict
        """
        timestamp = self.tz.localize(datetime.datetime.now()).timestamp()
        date = datetime.datetime.utcnow()
        data = bytearray("%d-%s" % (timestamp, data), "utf-8")
        hmac_digest = hmac.new(self.secret, data, "sha256").hexdigest()
        authorization_header = "Sign %s" % base64.b64encode(bytearray("%s:%s" % (self.uuid, hmac_digest), "utf-8")).decode("utf-8")
        headers = {
            "Date": date.strftime("%a, %d %b %Y %H:%M:%S"),
            "Authorization": authorization_header,
            "Content-Type": "application/json"
        }
        return headers
