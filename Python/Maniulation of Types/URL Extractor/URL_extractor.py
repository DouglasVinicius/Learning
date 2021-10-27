import re

class URL_extractor:

    def __init__(self, url, site_name, domain):
        self.__site_name = site_name
        self.__domain = domain
        self.__url = self.__url_sanitization(url)
        self.__url_validation()
        self.__separate_url()
        self.__collect_parameters()

    @property
    def base_url(self):
        return self.__base_url

    @property
    def parameters_url(self):
        return self.__parameters_url

    @property
    def domain(self):
        return self.__domain

    @property
    def site_name(self):
        return self.__site_name

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, new_url):
        self.__url = self.__url_sanitization(new_url)
        self.__url_validation()
        self.__separate_url()
        self.__collect_parameters()

    def __str__(self):
        return f"URL: {self.__url}" + "\n" + f"Base URL: {self.__base_url}" + "\n" + f"Parameters names: {self.__parameters_names}" + "\n" + f"Parameters values: {self.__parameters_values}"

    def __len__(self):
        return len(self.__url)

    def __eq__(self, other):
        return self.__url == other.url

    def __getitem__(self, item):
        return self.__url[item]

    def __url_validation(self):
        default_url = re.compile(f"(http(s)?://)?(www.)?{self.__site_name}{self.__domain}[a-z]*")
        match = default_url.match(self.__url)

        if((not self.__url) or (not match)):
            raise ValueError("Invalid URL!")

    def __url_sanitization(self, url):
        if(type(url) == str):
            url = url.strip()
            return url
        else:
            return ""

    def __separate_url(self):
        index_interrogation = self.__url.find("?")
        if(index_interrogation != -1):
            self.__base_url = self.__url[:index_interrogation]
            self.__parameters_url = self.__url[index_interrogation+1:]
        else:
            self.__base_url = self.__url
            self.__parameters_url = ""

    def __collect_parameters(self):
        parameters = self.__parameters_url.split("&")
        self.__parameters_names = []
        self.__parameters_values = []

        for parameter in parameters:
            index_equal = parameter.find("=")
            self.__parameters_names.append(parameter[:index_equal])
            self.__parameters_values.append(parameter[index_equal+1:])

    def get_parameter_value(self, parameter):
        try:
            index_parameter = self.__parameters_names.index(parameter)
            return self.__parameters_values[index_parameter]
        except:
            raise IndexError("This parameter don't exist!")

    def find_value_parameter(self, value):
        try:
            index_value = self.__parameters_values.index(value)
            return self.__parameters_names[index_value]
        except:
            raise IndexError("This value don't exist!")