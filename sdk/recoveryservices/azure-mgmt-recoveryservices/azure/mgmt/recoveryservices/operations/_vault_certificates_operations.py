# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import MixinABC, _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_create_request(
    subscription_id: str,
    resource_group_name: str,
    vault_name: str,
    certificate_name: str,
    *,
    json: Optional[_models.CertificateRequest] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )

class VaultCertificatesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservices.RecoveryServicesClient`'s
        :attr:`vault_certificates` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def create(
        self,
        resource_group_name: str,
        vault_name: str,
        certificate_name: str,
        certificate_request: _models.CertificateRequest,
        **kwargs: Any
    ) -> _models.VaultCertificateResponse:
        """Uploads a certificate for a resource.

        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param certificate_name: Certificate friendly name.
        :type certificate_name: str
        :param certificate_request: Input parameters for uploading the vault certificate.
        :type certificate_request: ~azure.mgmt.recoveryservices.models.CertificateRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VaultCertificateResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservices.models.VaultCertificateResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-04-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.VaultCertificateResponse]

        _json = self._serialize.body(certificate_request, 'CertificateRequest')

        request = build_create_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            certificate_name=certificate_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VaultCertificateResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName}"}  # type: ignore

