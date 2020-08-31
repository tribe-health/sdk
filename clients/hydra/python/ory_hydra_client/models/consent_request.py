# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.7.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class ConsentRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'acr': 'str',
        'challenge': 'str',
        'client': 'OAuth2Client',
        'context': 'object',
        'login_challenge': 'str',
        'login_session_id': 'str',
        'oidc_context': 'OpenIDConnectContext',
        'request_url': 'str',
        'requested_access_token_audience': 'list[str]',
        'requested_scope': 'list[str]',
        'skip': 'bool',
        'subject': 'str'
    }

    attribute_map = {
        'acr': 'acr',
        'challenge': 'challenge',
        'client': 'client',
        'context': 'context',
        'login_challenge': 'login_challenge',
        'login_session_id': 'login_session_id',
        'oidc_context': 'oidc_context',
        'request_url': 'request_url',
        'requested_access_token_audience': 'requested_access_token_audience',
        'requested_scope': 'requested_scope',
        'skip': 'skip',
        'subject': 'subject'
    }

    def __init__(self, acr=None, challenge=None, client=None, context=None, login_challenge=None, login_session_id=None, oidc_context=None, request_url=None, requested_access_token_audience=None, requested_scope=None, skip=None, subject=None, local_vars_configuration=None):  # noqa: E501
        """ConsentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acr = None
        self._challenge = None
        self._client = None
        self._context = None
        self._login_challenge = None
        self._login_session_id = None
        self._oidc_context = None
        self._request_url = None
        self._requested_access_token_audience = None
        self._requested_scope = None
        self._skip = None
        self._subject = None
        self.discriminator = None

        if acr is not None:
            self.acr = acr
        self.challenge = challenge
        if client is not None:
            self.client = client
        if context is not None:
            self.context = context
        if login_challenge is not None:
            self.login_challenge = login_challenge
        if login_session_id is not None:
            self.login_session_id = login_session_id
        if oidc_context is not None:
            self.oidc_context = oidc_context
        if request_url is not None:
            self.request_url = request_url
        if requested_access_token_audience is not None:
            self.requested_access_token_audience = requested_access_token_audience
        if requested_scope is not None:
            self.requested_scope = requested_scope
        if skip is not None:
            self.skip = skip
        if subject is not None:
            self.subject = subject

    @property
    def acr(self):
        """Gets the acr of this ConsentRequest.  # noqa: E501

        ACR represents the Authentication AuthorizationContext Class Reference value for this authentication session. You can use it to express that, for example, a user authenticated using two factor authentication.  # noqa: E501

        :return: The acr of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._acr

    @acr.setter
    def acr(self, acr):
        """Sets the acr of this ConsentRequest.

        ACR represents the Authentication AuthorizationContext Class Reference value for this authentication session. You can use it to express that, for example, a user authenticated using two factor authentication.  # noqa: E501

        :param acr: The acr of this ConsentRequest.  # noqa: E501
        :type: str
        """

        self._acr = acr

    @property
    def challenge(self):
        """Gets the challenge of this ConsentRequest.  # noqa: E501

        Challenge is the identifier (\"authorization challenge\") of the consent authorization request. It is used to identify the session.  # noqa: E501

        :return: The challenge of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this ConsentRequest.

        Challenge is the identifier (\"authorization challenge\") of the consent authorization request. It is used to identify the session.  # noqa: E501

        :param challenge: The challenge of this ConsentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and challenge is None:  # noqa: E501
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def client(self):
        """Gets the client of this ConsentRequest.  # noqa: E501


        :return: The client of this ConsentRequest.  # noqa: E501
        :rtype: OAuth2Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ConsentRequest.


        :param client: The client of this ConsentRequest.  # noqa: E501
        :type: OAuth2Client
        """

        self._client = client

    @property
    def context(self):
        """Gets the context of this ConsentRequest.  # noqa: E501


        :return: The context of this ConsentRequest.  # noqa: E501
        :rtype: object
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ConsentRequest.


        :param context: The context of this ConsentRequest.  # noqa: E501
        :type: object
        """

        self._context = context

    @property
    def login_challenge(self):
        """Gets the login_challenge of this ConsentRequest.  # noqa: E501

        LoginChallenge is the login challenge this consent challenge belongs to. It can be used to associate a login and consent request in the login & consent app.  # noqa: E501

        :return: The login_challenge of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._login_challenge

    @login_challenge.setter
    def login_challenge(self, login_challenge):
        """Sets the login_challenge of this ConsentRequest.

        LoginChallenge is the login challenge this consent challenge belongs to. It can be used to associate a login and consent request in the login & consent app.  # noqa: E501

        :param login_challenge: The login_challenge of this ConsentRequest.  # noqa: E501
        :type: str
        """

        self._login_challenge = login_challenge

    @property
    def login_session_id(self):
        """Gets the login_session_id of this ConsentRequest.  # noqa: E501

        LoginSessionID is the login session ID. If the user-agent reuses a login session (via cookie / remember flag) this ID will remain the same. If the user-agent did not have an existing authentication session (e.g. remember is false) this will be a new random value. This value is used as the \"sid\" parameter in the ID Token and in OIDC Front-/Back- channel logout. It's value can generally be used to associate consecutive login requests by a certain user.  # noqa: E501

        :return: The login_session_id of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._login_session_id

    @login_session_id.setter
    def login_session_id(self, login_session_id):
        """Sets the login_session_id of this ConsentRequest.

        LoginSessionID is the login session ID. If the user-agent reuses a login session (via cookie / remember flag) this ID will remain the same. If the user-agent did not have an existing authentication session (e.g. remember is false) this will be a new random value. This value is used as the \"sid\" parameter in the ID Token and in OIDC Front-/Back- channel logout. It's value can generally be used to associate consecutive login requests by a certain user.  # noqa: E501

        :param login_session_id: The login_session_id of this ConsentRequest.  # noqa: E501
        :type: str
        """

        self._login_session_id = login_session_id

    @property
    def oidc_context(self):
        """Gets the oidc_context of this ConsentRequest.  # noqa: E501


        :return: The oidc_context of this ConsentRequest.  # noqa: E501
        :rtype: OpenIDConnectContext
        """
        return self._oidc_context

    @oidc_context.setter
    def oidc_context(self, oidc_context):
        """Sets the oidc_context of this ConsentRequest.


        :param oidc_context: The oidc_context of this ConsentRequest.  # noqa: E501
        :type: OpenIDConnectContext
        """

        self._oidc_context = oidc_context

    @property
    def request_url(self):
        """Gets the request_url of this ConsentRequest.  # noqa: E501

        RequestURL is the original OAuth 2.0 Authorization URL requested by the OAuth 2.0 client. It is the URL which initiates the OAuth 2.0 Authorization Code or OAuth 2.0 Implicit flow. This URL is typically not needed, but might come in handy if you want to deal with additional request parameters.  # noqa: E501

        :return: The request_url of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this ConsentRequest.

        RequestURL is the original OAuth 2.0 Authorization URL requested by the OAuth 2.0 client. It is the URL which initiates the OAuth 2.0 Authorization Code or OAuth 2.0 Implicit flow. This URL is typically not needed, but might come in handy if you want to deal with additional request parameters.  # noqa: E501

        :param request_url: The request_url of this ConsentRequest.  # noqa: E501
        :type: str
        """

        self._request_url = request_url

    @property
    def requested_access_token_audience(self):
        """Gets the requested_access_token_audience of this ConsentRequest.  # noqa: E501


        :return: The requested_access_token_audience of this ConsentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._requested_access_token_audience

    @requested_access_token_audience.setter
    def requested_access_token_audience(self, requested_access_token_audience):
        """Sets the requested_access_token_audience of this ConsentRequest.


        :param requested_access_token_audience: The requested_access_token_audience of this ConsentRequest.  # noqa: E501
        :type: list[str]
        """

        self._requested_access_token_audience = requested_access_token_audience

    @property
    def requested_scope(self):
        """Gets the requested_scope of this ConsentRequest.  # noqa: E501


        :return: The requested_scope of this ConsentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._requested_scope

    @requested_scope.setter
    def requested_scope(self, requested_scope):
        """Sets the requested_scope of this ConsentRequest.


        :param requested_scope: The requested_scope of this ConsentRequest.  # noqa: E501
        :type: list[str]
        """

        self._requested_scope = requested_scope

    @property
    def skip(self):
        """Gets the skip of this ConsentRequest.  # noqa: E501

        Skip, if true, implies that the client has requested the same scopes from the same user previously. If true, you must not ask the user to grant the requested scopes. You must however either allow or deny the consent request using the usual API call.  # noqa: E501

        :return: The skip of this ConsentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this ConsentRequest.

        Skip, if true, implies that the client has requested the same scopes from the same user previously. If true, you must not ask the user to grant the requested scopes. You must however either allow or deny the consent request using the usual API call.  # noqa: E501

        :param skip: The skip of this ConsentRequest.  # noqa: E501
        :type: bool
        """

        self._skip = skip

    @property
    def subject(self):
        """Gets the subject of this ConsentRequest.  # noqa: E501

        Subject is the user ID of the end-user that authenticated. Now, that end user needs to grant or deny the scope requested by the OAuth 2.0 client.  # noqa: E501

        :return: The subject of this ConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ConsentRequest.

        Subject is the user ID of the end-user that authenticated. Now, that end user needs to grant or deny the scope requested by the OAuth 2.0 client.  # noqa: E501

        :param subject: The subject of this ConsentRequest.  # noqa: E501
        :type: str
        """

        self._subject = subject

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConsentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentRequest):
            return True

        return self.to_dict() != other.to_dict()
