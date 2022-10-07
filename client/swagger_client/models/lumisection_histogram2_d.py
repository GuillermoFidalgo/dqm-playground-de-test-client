# coding: utf-8

"""
    MLPlayground

    API  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LumisectionHistogram2D(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'run': 'int',
        'lumisection': 'int',
        'title': 'str',
        'entries': 'int',
        'data': 'list[list[float]]',
        'x_min': 'float',
        'x_max': 'float',
        'x_bin': 'int',
        'y_max': 'float',
        'y_min': 'float',
        'y_bin': 'int',
        'source_data_file': 'int'
    }

    attribute_map = {
        'id': 'id',
        'run': 'run',
        'lumisection': 'lumisection',
        'title': 'title',
        'entries': 'entries',
        'data': 'data',
        'x_min': 'x_min',
        'x_max': 'x_max',
        'x_bin': 'x_bin',
        'y_max': 'y_max',
        'y_min': 'y_min',
        'y_bin': 'y_bin',
        'source_data_file': 'source_data_file'
    }

    def __init__(self, id=None, run=None, lumisection=None, title=None, entries=None, data=None, x_min=None, x_max=None, x_bin=None, y_max=None, y_min=None, y_bin=None, source_data_file=None):  # noqa: E501
        """LumisectionHistogram2D - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._run = None
        self._lumisection = None
        self._title = None
        self._entries = None
        self._data = None
        self._x_min = None
        self._x_max = None
        self._x_bin = None
        self._y_max = None
        self._y_min = None
        self._y_bin = None
        self._source_data_file = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if run is not None:
            self.run = run
        if lumisection is not None:
            self.lumisection = lumisection
        self.title = title
        if entries is not None:
            self.entries = entries
        if data is not None:
            self.data = data
        if x_min is not None:
            self.x_min = x_min
        if x_max is not None:
            self.x_max = x_max
        if x_bin is not None:
            self.x_bin = x_bin
        if y_max is not None:
            self.y_max = y_max
        if y_min is not None:
            self.y_min = y_min
        if y_bin is not None:
            self.y_bin = y_bin
        if source_data_file is not None:
            self.source_data_file = source_data_file

    @property
    def id(self):
        """Gets the id of this LumisectionHistogram2D.  # noqa: E501


        :return: The id of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LumisectionHistogram2D.


        :param id: The id of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def run(self):
        """Gets the run of this LumisectionHistogram2D.  # noqa: E501


        :return: The run of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this LumisectionHistogram2D.


        :param run: The run of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._run = run

    @property
    def lumisection(self):
        """Gets the lumisection of this LumisectionHistogram2D.  # noqa: E501


        :return: The lumisection of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._lumisection

    @lumisection.setter
    def lumisection(self, lumisection):
        """Sets the lumisection of this LumisectionHistogram2D.


        :param lumisection: The lumisection of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._lumisection = lumisection

    @property
    def title(self):
        """Gets the title of this LumisectionHistogram2D.  # noqa: E501


        :return: The title of this LumisectionHistogram2D.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LumisectionHistogram2D.


        :param title: The title of this LumisectionHistogram2D.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def entries(self):
        """Gets the entries of this LumisectionHistogram2D.  # noqa: E501


        :return: The entries of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this LumisectionHistogram2D.


        :param entries: The entries of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._entries = entries

    @property
    def data(self):
        """Gets the data of this LumisectionHistogram2D.  # noqa: E501


        :return: The data of this LumisectionHistogram2D.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this LumisectionHistogram2D.


        :param data: The data of this LumisectionHistogram2D.  # noqa: E501
        :type: list[list[float]]
        """

        self._data = data

    @property
    def x_min(self):
        """Gets the x_min of this LumisectionHistogram2D.  # noqa: E501


        :return: The x_min of this LumisectionHistogram2D.  # noqa: E501
        :rtype: float
        """
        return self._x_min

    @x_min.setter
    def x_min(self, x_min):
        """Sets the x_min of this LumisectionHistogram2D.


        :param x_min: The x_min of this LumisectionHistogram2D.  # noqa: E501
        :type: float
        """

        self._x_min = x_min

    @property
    def x_max(self):
        """Gets the x_max of this LumisectionHistogram2D.  # noqa: E501


        :return: The x_max of this LumisectionHistogram2D.  # noqa: E501
        :rtype: float
        """
        return self._x_max

    @x_max.setter
    def x_max(self, x_max):
        """Sets the x_max of this LumisectionHistogram2D.


        :param x_max: The x_max of this LumisectionHistogram2D.  # noqa: E501
        :type: float
        """

        self._x_max = x_max

    @property
    def x_bin(self):
        """Gets the x_bin of this LumisectionHistogram2D.  # noqa: E501


        :return: The x_bin of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._x_bin

    @x_bin.setter
    def x_bin(self, x_bin):
        """Sets the x_bin of this LumisectionHistogram2D.


        :param x_bin: The x_bin of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._x_bin = x_bin

    @property
    def y_max(self):
        """Gets the y_max of this LumisectionHistogram2D.  # noqa: E501


        :return: The y_max of this LumisectionHistogram2D.  # noqa: E501
        :rtype: float
        """
        return self._y_max

    @y_max.setter
    def y_max(self, y_max):
        """Sets the y_max of this LumisectionHistogram2D.


        :param y_max: The y_max of this LumisectionHistogram2D.  # noqa: E501
        :type: float
        """

        self._y_max = y_max

    @property
    def y_min(self):
        """Gets the y_min of this LumisectionHistogram2D.  # noqa: E501


        :return: The y_min of this LumisectionHistogram2D.  # noqa: E501
        :rtype: float
        """
        return self._y_min

    @y_min.setter
    def y_min(self, y_min):
        """Sets the y_min of this LumisectionHistogram2D.


        :param y_min: The y_min of this LumisectionHistogram2D.  # noqa: E501
        :type: float
        """

        self._y_min = y_min

    @property
    def y_bin(self):
        """Gets the y_bin of this LumisectionHistogram2D.  # noqa: E501


        :return: The y_bin of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._y_bin

    @y_bin.setter
    def y_bin(self, y_bin):
        """Sets the y_bin of this LumisectionHistogram2D.


        :param y_bin: The y_bin of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._y_bin = y_bin

    @property
    def source_data_file(self):
        """Gets the source_data_file of this LumisectionHistogram2D.  # noqa: E501

        Source data file that the specific Histogram was read from, if any  # noqa: E501

        :return: The source_data_file of this LumisectionHistogram2D.  # noqa: E501
        :rtype: int
        """
        return self._source_data_file

    @source_data_file.setter
    def source_data_file(self, source_data_file):
        """Sets the source_data_file of this LumisectionHistogram2D.

        Source data file that the specific Histogram was read from, if any  # noqa: E501

        :param source_data_file: The source_data_file of this LumisectionHistogram2D.  # noqa: E501
        :type: int
        """

        self._source_data_file = source_data_file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LumisectionHistogram2D, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LumisectionHistogram2D):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
