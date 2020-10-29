# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.9.0-alpha.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class WellKnown(object):
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
        'authorization_endpoint': 'str',
        'backchannel_logout_session_supported': 'bool',
        'backchannel_logout_supported': 'bool',
        'claims_parameter_supported': 'bool',
        'claims_supported': 'list[str]',
        'end_session_endpoint': 'str',
        'frontchannel_logout_session_supported': 'bool',
        'frontchannel_logout_supported': 'bool',
        'grant_types_supported': 'list[str]',
        'id_token_signing_alg_values_supported': 'list[str]',
        'issuer': 'str',
        'jwks_uri': 'str',
        'registration_endpoint': 'str',
        'request_parameter_supported': 'bool',
        'request_uri_parameter_supported': 'bool',
        'require_request_uri_registration': 'bool',
        'response_modes_supported': 'list[str]',
        'response_types_supported': 'list[str]',
        'revocation_endpoint': 'str',
        'scopes_supported': 'list[str]',
        'subject_types_supported': 'list[str]',
        'token_endpoint': 'str',
        'token_endpoint_auth_methods_supported': 'list[str]',
        'userinfo_endpoint': 'str',
        'userinfo_signing_alg_values_supported': 'list[str]'
    }

    attribute_map = {
        'authorization_endpoint': 'authorization_endpoint',
        'backchannel_logout_session_supported': 'backchannel_logout_session_supported',
        'backchannel_logout_supported': 'backchannel_logout_supported',
        'claims_parameter_supported': 'claims_parameter_supported',
        'claims_supported': 'claims_supported',
        'end_session_endpoint': 'end_session_endpoint',
        'frontchannel_logout_session_supported': 'frontchannel_logout_session_supported',
        'frontchannel_logout_supported': 'frontchannel_logout_supported',
        'grant_types_supported': 'grant_types_supported',
        'id_token_signing_alg_values_supported': 'id_token_signing_alg_values_supported',
        'issuer': 'issuer',
        'jwks_uri': 'jwks_uri',
        'registration_endpoint': 'registration_endpoint',
        'request_parameter_supported': 'request_parameter_supported',
        'request_uri_parameter_supported': 'request_uri_parameter_supported',
        'require_request_uri_registration': 'require_request_uri_registration',
        'response_modes_supported': 'response_modes_supported',
        'response_types_supported': 'response_types_supported',
        'revocation_endpoint': 'revocation_endpoint',
        'scopes_supported': 'scopes_supported',
        'subject_types_supported': 'subject_types_supported',
        'token_endpoint': 'token_endpoint',
        'token_endpoint_auth_methods_supported': 'token_endpoint_auth_methods_supported',
        'userinfo_endpoint': 'userinfo_endpoint',
        'userinfo_signing_alg_values_supported': 'userinfo_signing_alg_values_supported'
    }

    def __init__(self, authorization_endpoint=None, backchannel_logout_session_supported=None, backchannel_logout_supported=None, claims_parameter_supported=None, claims_supported=None, end_session_endpoint=None, frontchannel_logout_session_supported=None, frontchannel_logout_supported=None, grant_types_supported=None, id_token_signing_alg_values_supported=None, issuer=None, jwks_uri=None, registration_endpoint=None, request_parameter_supported=None, request_uri_parameter_supported=None, require_request_uri_registration=None, response_modes_supported=None, response_types_supported=None, revocation_endpoint=None, scopes_supported=None, subject_types_supported=None, token_endpoint=None, token_endpoint_auth_methods_supported=None, userinfo_endpoint=None, userinfo_signing_alg_values_supported=None, local_vars_configuration=None):  # noqa: E501
        """WellKnown - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorization_endpoint = None
        self._backchannel_logout_session_supported = None
        self._backchannel_logout_supported = None
        self._claims_parameter_supported = None
        self._claims_supported = None
        self._end_session_endpoint = None
        self._frontchannel_logout_session_supported = None
        self._frontchannel_logout_supported = None
        self._grant_types_supported = None
        self._id_token_signing_alg_values_supported = None
        self._issuer = None
        self._jwks_uri = None
        self._registration_endpoint = None
        self._request_parameter_supported = None
        self._request_uri_parameter_supported = None
        self._require_request_uri_registration = None
        self._response_modes_supported = None
        self._response_types_supported = None
        self._revocation_endpoint = None
        self._scopes_supported = None
        self._subject_types_supported = None
        self._token_endpoint = None
        self._token_endpoint_auth_methods_supported = None
        self._userinfo_endpoint = None
        self._userinfo_signing_alg_values_supported = None
        self.discriminator = None

        self.authorization_endpoint = authorization_endpoint
        if backchannel_logout_session_supported is not None:
            self.backchannel_logout_session_supported = backchannel_logout_session_supported
        if backchannel_logout_supported is not None:
            self.backchannel_logout_supported = backchannel_logout_supported
        if claims_parameter_supported is not None:
            self.claims_parameter_supported = claims_parameter_supported
        if claims_supported is not None:
            self.claims_supported = claims_supported
        if end_session_endpoint is not None:
            self.end_session_endpoint = end_session_endpoint
        if frontchannel_logout_session_supported is not None:
            self.frontchannel_logout_session_supported = frontchannel_logout_session_supported
        if frontchannel_logout_supported is not None:
            self.frontchannel_logout_supported = frontchannel_logout_supported
        if grant_types_supported is not None:
            self.grant_types_supported = grant_types_supported
        self.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self.issuer = issuer
        self.jwks_uri = jwks_uri
        if registration_endpoint is not None:
            self.registration_endpoint = registration_endpoint
        if request_parameter_supported is not None:
            self.request_parameter_supported = request_parameter_supported
        if request_uri_parameter_supported is not None:
            self.request_uri_parameter_supported = request_uri_parameter_supported
        if require_request_uri_registration is not None:
            self.require_request_uri_registration = require_request_uri_registration
        if response_modes_supported is not None:
            self.response_modes_supported = response_modes_supported
        self.response_types_supported = response_types_supported
        if revocation_endpoint is not None:
            self.revocation_endpoint = revocation_endpoint
        if scopes_supported is not None:
            self.scopes_supported = scopes_supported
        self.subject_types_supported = subject_types_supported
        self.token_endpoint = token_endpoint
        if token_endpoint_auth_methods_supported is not None:
            self.token_endpoint_auth_methods_supported = token_endpoint_auth_methods_supported
        if userinfo_endpoint is not None:
            self.userinfo_endpoint = userinfo_endpoint
        if userinfo_signing_alg_values_supported is not None:
            self.userinfo_signing_alg_values_supported = userinfo_signing_alg_values_supported

    @property
    def authorization_endpoint(self):
        """Gets the authorization_endpoint of this WellKnown.  # noqa: E501

        URL of the OP's OAuth 2.0 Authorization Endpoint.  # noqa: E501

        :return: The authorization_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """Sets the authorization_endpoint of this WellKnown.

        URL of the OP's OAuth 2.0 Authorization Endpoint.  # noqa: E501

        :param authorization_endpoint: The authorization_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and authorization_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `authorization_endpoint`, must not be `None`")  # noqa: E501

        self._authorization_endpoint = authorization_endpoint

    @property
    def backchannel_logout_session_supported(self):
        """Gets the backchannel_logout_session_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP  # noqa: E501

        :return: The backchannel_logout_session_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._backchannel_logout_session_supported

    @backchannel_logout_session_supported.setter
    def backchannel_logout_session_supported(self, backchannel_logout_session_supported):
        """Sets the backchannel_logout_session_supported of this WellKnown.

        Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP  # noqa: E501

        :param backchannel_logout_session_supported: The backchannel_logout_session_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._backchannel_logout_session_supported = backchannel_logout_session_supported

    @property
    def backchannel_logout_supported(self):
        """Gets the backchannel_logout_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP supports back-channel logout, with true indicating support.  # noqa: E501

        :return: The backchannel_logout_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._backchannel_logout_supported

    @backchannel_logout_supported.setter
    def backchannel_logout_supported(self, backchannel_logout_supported):
        """Sets the backchannel_logout_supported of this WellKnown.

        Boolean value specifying whether the OP supports back-channel logout, with true indicating support.  # noqa: E501

        :param backchannel_logout_supported: The backchannel_logout_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._backchannel_logout_supported = backchannel_logout_supported

    @property
    def claims_parameter_supported(self):
        """Gets the claims_parameter_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support.  # noqa: E501

        :return: The claims_parameter_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._claims_parameter_supported

    @claims_parameter_supported.setter
    def claims_parameter_supported(self, claims_parameter_supported):
        """Sets the claims_parameter_supported of this WellKnown.

        Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support.  # noqa: E501

        :param claims_parameter_supported: The claims_parameter_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._claims_parameter_supported = claims_parameter_supported

    @property
    def claims_supported(self):
        """Gets the claims_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for. Note that for privacy or other reasons, this might not be an exhaustive list.  # noqa: E501

        :return: The claims_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._claims_supported

    @claims_supported.setter
    def claims_supported(self, claims_supported):
        """Sets the claims_supported of this WellKnown.

        JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for. Note that for privacy or other reasons, this might not be an exhaustive list.  # noqa: E501

        :param claims_supported: The claims_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._claims_supported = claims_supported

    @property
    def end_session_endpoint(self):
        """Gets the end_session_endpoint of this WellKnown.  # noqa: E501

        URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.  # noqa: E501

        :return: The end_session_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._end_session_endpoint

    @end_session_endpoint.setter
    def end_session_endpoint(self, end_session_endpoint):
        """Sets the end_session_endpoint of this WellKnown.

        URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.  # noqa: E501

        :param end_session_endpoint: The end_session_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """

        self._end_session_endpoint = end_session_endpoint

    @property
    def frontchannel_logout_session_supported(self):
        """Gets the frontchannel_logout_session_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP can pass iss (issuer) and sid (session ID) query parameters to identify the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also included in ID Tokens issued by the OP.  # noqa: E501

        :return: The frontchannel_logout_session_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._frontchannel_logout_session_supported

    @frontchannel_logout_session_supported.setter
    def frontchannel_logout_session_supported(self, frontchannel_logout_session_supported):
        """Sets the frontchannel_logout_session_supported of this WellKnown.

        Boolean value specifying whether the OP can pass iss (issuer) and sid (session ID) query parameters to identify the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also included in ID Tokens issued by the OP.  # noqa: E501

        :param frontchannel_logout_session_supported: The frontchannel_logout_session_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._frontchannel_logout_session_supported = frontchannel_logout_session_supported

    @property
    def frontchannel_logout_supported(self):
        """Gets the frontchannel_logout_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support.  # noqa: E501

        :return: The frontchannel_logout_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._frontchannel_logout_supported

    @frontchannel_logout_supported.setter
    def frontchannel_logout_supported(self, frontchannel_logout_supported):
        """Sets the frontchannel_logout_supported of this WellKnown.

        Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support.  # noqa: E501

        :param frontchannel_logout_supported: The frontchannel_logout_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._frontchannel_logout_supported = frontchannel_logout_supported

    @property
    def grant_types_supported(self):
        """Gets the grant_types_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.  # noqa: E501

        :return: The grant_types_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_types_supported

    @grant_types_supported.setter
    def grant_types_supported(self, grant_types_supported):
        """Sets the grant_types_supported of this WellKnown.

        JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.  # noqa: E501

        :param grant_types_supported: The grant_types_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._grant_types_supported = grant_types_supported

    @property
    def id_token_signing_alg_values_supported(self):
        """Gets the id_token_signing_alg_values_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.  # noqa: E501

        :return: The id_token_signing_alg_values_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_token_signing_alg_values_supported

    @id_token_signing_alg_values_supported.setter
    def id_token_signing_alg_values_supported(self, id_token_signing_alg_values_supported):
        """Sets the id_token_signing_alg_values_supported of this WellKnown.

        JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.  # noqa: E501

        :param id_token_signing_alg_values_supported: The id_token_signing_alg_values_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and id_token_signing_alg_values_supported is None:  # noqa: E501
            raise ValueError("Invalid value for `id_token_signing_alg_values_supported`, must not be `None`")  # noqa: E501

        self._id_token_signing_alg_values_supported = id_token_signing_alg_values_supported

    @property
    def issuer(self):
        """Gets the issuer of this WellKnown.  # noqa: E501

        URL using the https scheme with no query or fragment component that the OP asserts as its IssuerURL Identifier. If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.  # noqa: E501

        :return: The issuer of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this WellKnown.

        URL using the https scheme with no query or fragment component that the OP asserts as its IssuerURL Identifier. If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.  # noqa: E501

        :param issuer: The issuer of this WellKnown.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this WellKnown.  # noqa: E501

        URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.  # noqa: E501

        :return: The jwks_uri of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this WellKnown.

        URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.  # noqa: E501

        :param jwks_uri: The jwks_uri of this WellKnown.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jwks_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `jwks_uri`, must not be `None`")  # noqa: E501

        self._jwks_uri = jwks_uri

    @property
    def registration_endpoint(self):
        """Gets the registration_endpoint of this WellKnown.  # noqa: E501

        URL of the OP's Dynamic Client Registration Endpoint.  # noqa: E501

        :return: The registration_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._registration_endpoint

    @registration_endpoint.setter
    def registration_endpoint(self, registration_endpoint):
        """Sets the registration_endpoint of this WellKnown.

        URL of the OP's Dynamic Client Registration Endpoint.  # noqa: E501

        :param registration_endpoint: The registration_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """

        self._registration_endpoint = registration_endpoint

    @property
    def request_parameter_supported(self):
        """Gets the request_parameter_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP supports use of the request parameter, with true indicating support.  # noqa: E501

        :return: The request_parameter_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._request_parameter_supported

    @request_parameter_supported.setter
    def request_parameter_supported(self, request_parameter_supported):
        """Sets the request_parameter_supported of this WellKnown.

        Boolean value specifying whether the OP supports use of the request parameter, with true indicating support.  # noqa: E501

        :param request_parameter_supported: The request_parameter_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._request_parameter_supported = request_parameter_supported

    @property
    def request_uri_parameter_supported(self):
        """Gets the request_uri_parameter_supported of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support.  # noqa: E501

        :return: The request_uri_parameter_supported of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._request_uri_parameter_supported

    @request_uri_parameter_supported.setter
    def request_uri_parameter_supported(self, request_uri_parameter_supported):
        """Sets the request_uri_parameter_supported of this WellKnown.

        Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support.  # noqa: E501

        :param request_uri_parameter_supported: The request_uri_parameter_supported of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._request_uri_parameter_supported = request_uri_parameter_supported

    @property
    def require_request_uri_registration(self):
        """Gets the require_request_uri_registration of this WellKnown.  # noqa: E501

        Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter.  # noqa: E501

        :return: The require_request_uri_registration of this WellKnown.  # noqa: E501
        :rtype: bool
        """
        return self._require_request_uri_registration

    @require_request_uri_registration.setter
    def require_request_uri_registration(self, require_request_uri_registration):
        """Sets the require_request_uri_registration of this WellKnown.

        Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter.  # noqa: E501

        :param require_request_uri_registration: The require_request_uri_registration of this WellKnown.  # noqa: E501
        :type: bool
        """

        self._require_request_uri_registration = require_request_uri_registration

    @property
    def response_modes_supported(self):
        """Gets the response_modes_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports.  # noqa: E501

        :return: The response_modes_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_modes_supported

    @response_modes_supported.setter
    def response_modes_supported(self, response_modes_supported):
        """Sets the response_modes_supported of this WellKnown.

        JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports.  # noqa: E501

        :param response_modes_supported: The response_modes_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._response_modes_supported = response_modes_supported

    @property
    def response_types_supported(self):
        """Gets the response_types_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.  # noqa: E501

        :return: The response_types_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_types_supported

    @response_types_supported.setter
    def response_types_supported(self, response_types_supported):
        """Sets the response_types_supported of this WellKnown.

        JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.  # noqa: E501

        :param response_types_supported: The response_types_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and response_types_supported is None:  # noqa: E501
            raise ValueError("Invalid value for `response_types_supported`, must not be `None`")  # noqa: E501

        self._response_types_supported = response_types_supported

    @property
    def revocation_endpoint(self):
        """Gets the revocation_endpoint of this WellKnown.  # noqa: E501

        URL of the authorization server's OAuth 2.0 revocation endpoint.  # noqa: E501

        :return: The revocation_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._revocation_endpoint

    @revocation_endpoint.setter
    def revocation_endpoint(self, revocation_endpoint):
        """Sets the revocation_endpoint of this WellKnown.

        URL of the authorization server's OAuth 2.0 revocation endpoint.  # noqa: E501

        :param revocation_endpoint: The revocation_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """

        self._revocation_endpoint = revocation_endpoint

    @property
    def scopes_supported(self):
        """Gets the scopes_supported of this WellKnown.  # noqa: E501

        SON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports. The server MUST support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this parameter is used  # noqa: E501

        :return: The scopes_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes_supported

    @scopes_supported.setter
    def scopes_supported(self, scopes_supported):
        """Sets the scopes_supported of this WellKnown.

        SON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports. The server MUST support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this parameter is used  # noqa: E501

        :param scopes_supported: The scopes_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._scopes_supported = scopes_supported

    @property
    def subject_types_supported(self):
        """Gets the subject_types_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.  # noqa: E501

        :return: The subject_types_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_types_supported

    @subject_types_supported.setter
    def subject_types_supported(self, subject_types_supported):
        """Sets the subject_types_supported of this WellKnown.

        JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.  # noqa: E501

        :param subject_types_supported: The subject_types_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and subject_types_supported is None:  # noqa: E501
            raise ValueError("Invalid value for `subject_types_supported`, must not be `None`")  # noqa: E501

        self._subject_types_supported = subject_types_supported

    @property
    def token_endpoint(self):
        """Gets the token_endpoint of this WellKnown.  # noqa: E501

        URL of the OP's OAuth 2.0 Token Endpoint  # noqa: E501

        :return: The token_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        """Sets the token_endpoint of this WellKnown.

        URL of the OP's OAuth 2.0 Token Endpoint  # noqa: E501

        :param token_endpoint: The token_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `token_endpoint`, must not be `None`")  # noqa: E501

        self._token_endpoint = token_endpoint

    @property
    def token_endpoint_auth_methods_supported(self):
        """Gets the token_endpoint_auth_methods_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of Client Authentication methods supported by this Token Endpoint. The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0  # noqa: E501

        :return: The token_endpoint_auth_methods_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._token_endpoint_auth_methods_supported

    @token_endpoint_auth_methods_supported.setter
    def token_endpoint_auth_methods_supported(self, token_endpoint_auth_methods_supported):
        """Sets the token_endpoint_auth_methods_supported of this WellKnown.

        JSON array containing a list of Client Authentication methods supported by this Token Endpoint. The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0  # noqa: E501

        :param token_endpoint_auth_methods_supported: The token_endpoint_auth_methods_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._token_endpoint_auth_methods_supported = token_endpoint_auth_methods_supported

    @property
    def userinfo_endpoint(self):
        """Gets the userinfo_endpoint of this WellKnown.  # noqa: E501

        URL of the OP's UserInfo Endpoint.  # noqa: E501

        :return: The userinfo_endpoint of this WellKnown.  # noqa: E501
        :rtype: str
        """
        return self._userinfo_endpoint

    @userinfo_endpoint.setter
    def userinfo_endpoint(self, userinfo_endpoint):
        """Sets the userinfo_endpoint of this WellKnown.

        URL of the OP's UserInfo Endpoint.  # noqa: E501

        :param userinfo_endpoint: The userinfo_endpoint of this WellKnown.  # noqa: E501
        :type: str
        """

        self._userinfo_endpoint = userinfo_endpoint

    @property
    def userinfo_signing_alg_values_supported(self):
        """Gets the userinfo_signing_alg_values_supported of this WellKnown.  # noqa: E501

        JSON array containing a list of the JWS [JWS] signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].  # noqa: E501

        :return: The userinfo_signing_alg_values_supported of this WellKnown.  # noqa: E501
        :rtype: list[str]
        """
        return self._userinfo_signing_alg_values_supported

    @userinfo_signing_alg_values_supported.setter
    def userinfo_signing_alg_values_supported(self, userinfo_signing_alg_values_supported):
        """Sets the userinfo_signing_alg_values_supported of this WellKnown.

        JSON array containing a list of the JWS [JWS] signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].  # noqa: E501

        :param userinfo_signing_alg_values_supported: The userinfo_signing_alg_values_supported of this WellKnown.  # noqa: E501
        :type: list[str]
        """

        self._userinfo_signing_alg_values_supported = userinfo_signing_alg_values_supported

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
        if not isinstance(other, WellKnown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WellKnown):
            return True

        return self.to_dict() != other.to_dict()
