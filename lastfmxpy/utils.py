# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

import urllib.parse
from uuid import uuid4


class Utils:
    @staticmethod
    def parse_params_by_json(data: dict) -> str:
        """
        Parse parameters from a JSON data dictionary into a URL-encoded string.

        Args:
            data (dict): A dictionary containing parameter key-value pairs.

        Returns:
            str: A URL-encoded string of parameters.

        Example:
            >>> parsed_params = Utils.parse_params_by_json({
            ...     "name": "John Doe",
            ...     "age": 20
            ... })
            >>>
            >>> print(parsed_params)
            'param1=value1&param2=value2'
        """
        params = []

        for key, value in data.items():
            params.append(f"&{key}={urllib.parse.quote(str(value))}")

        return "".join(params).lstrip("&")

    @staticmethod
    def get_headers():
        return {
            "User-Agent": f"Mozilla/5.0 (Windows NT) {uuid4()}"
        }

    @staticmethod
    def remove_none_values(data: dict) -> dict:
        """
        Description:
            This static method is designed to remove key-value pairs with None values from a given dictionary.

        Parameters:
            - self: The instance of the class (implicitly passed due to being a static method).
            - d (dict): The input dictionary from which None values need to be removed.

        Returns:
            dict: A new dictionary containing only the key-value pairs where the values are not None.

        Example:
            ```python
            # Usage Example
            my_dict = {'a': 1, 'b': None, 'c': 'hello', 'd': None}
            result = Utils.remove_none_values(my_dict)
            print(result)
            ```
            Output:
            ```
            {'a': 1, 'c': 'hello'}
            ```
        """
        return {
            key: value for key, value in data.items() if value is not None
        }
