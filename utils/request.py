import requests
import allure

from dataclasses import dataclass
from utils.project_logger import LogConfig
from loguru import logger


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:

    LogConfig.set_logger_config()

    @allure.step("Send get request to '{1}'")
    def get(self, url):
        response = requests.get(url)
        logger. info(f"Send get request to {url}")
        return self.__get_responses(response)

    @allure.step("Send post request to '{1}' with '{2}'")
    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        logger.info(f"Send post request with {payload} to {url}")
        return self.__get_responses(response)

    @allure.step("Send put request to '{1}' with '{2}'")
    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=headers)
        logger.info(f"Send put request with {payload} to {url}")
        return self.__get_responses(response)

    @allure.step("Send patch request to '{1}' with '{2}'")
    def patch(self, url, payload, headers):
        response = requests.patch(url, data=payload, headers=headers)
        logger.info(f"Send patch request with {payload} to {url}")
        return self.__get_responses(response)

    @allure.step("Send delete request to '{1}'")
    def delete(self, url):
        response = requests.delete(url)
        logger.info(f"Send delete request to {url}")
        return self.__get_responses(response)

    @allure.step("Get response from service")
    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers
        logger.info(f"Returned status code {status_code}")
        logger.info(f"Returned headers {headers}")
        logger.info(f"Returned response body {as_dict}")
        return Response(
            status_code, text, as_dict, headers
        )