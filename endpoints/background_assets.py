from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetsEndpoint(Endpoint):
    path = '/v1/backgroundAssets'

    def create(self, request: BackgroundAssetCreateRequest) -> BackgroundAssetResponse:
        '''Create the resource.

        :param request: BackgroundAsset representation
        :type request: BackgroundAssetCreateRequest

        :returns: Single BackgroundAsset
        :rtype: BackgroundAssetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BackgroundAssetResponse.parse_obj(json)

class BackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}'

    @endpoint('/v1/backgroundAssets/{id}/versions')
    def versions(self) -> VersionsOfBackgroundAssetEndpoint:
        return VersionsOfBackgroundAssetEndpoint(self.id, self.session)
        
    @endpoint('/v1/backgroundAssets/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfBackgroundAssetEndpoint:
        return VersionsLinkagesOfBackgroundAssetEndpoint(self.id, self.session)
        
    def fields(self, *, background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]]=None) -> BackgroundAssetEndpoint:
        '''Fields to return for included related types.

        :param background_asset: the fields to include for returned resources of type backgroundAssets
        :type background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetEndpoint
        '''
        if background_asset: self._set_fields('backgroundAssets',background_asset if type(background_asset) is list else [background_asset])
        return self
        
    class Include(StringEnum):
        INTERNAL_BETA_VERSION = 'internalBetaVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BackgroundAssetResponse:
        '''Get the resource.

        :returns: Single BackgroundAsset
        :rtype: BackgroundAssetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetResponse.parse_obj(json)

class VersionsLinkagesOfBackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfBackgroundAssetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfBackgroundAssetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BackgroundAssetVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionsLinkagesResponse.parse_obj(json)

class VersionsOfBackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}/versions'

    def fields(self, *, background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]]=None, background_asset_version_internal_beta_release: Union[BackgroundAssetVersionInternalBetaReleaseField, list[BackgroundAssetVersionInternalBetaReleaseField]]=None, background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]]=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Fields to return for included related types.

        :param background_asset_version: the fields to include for returned resources of type backgroundAssetVersions
        :type background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]] = None

        :param background_asset_version_internal_beta_release: the fields to include for returned resources of type backgroundAssetVersionInternalBetaReleases
        :type background_asset_version_internal_beta_release: Union[BackgroundAssetVersionInternalBetaReleaseField, list[BackgroundAssetVersionInternalBetaReleaseField]] = None

        :param background_asset_upload_file: the fields to include for returned resources of type backgroundAssetUploadFiles
        :type background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if background_asset_version: self._set_fields('backgroundAssetVersions',background_asset_version if type(background_asset_version) is list else [background_asset_version])
        if background_asset_version_internal_beta_release: self._set_fields('backgroundAssetVersionInternalBetaReleases',background_asset_version_internal_beta_release if type(background_asset_version_internal_beta_release) is list else [background_asset_version_internal_beta_release])
        if background_asset_upload_file: self._set_fields('backgroundAssetUploadFiles',background_asset_upload_file if type(background_asset_upload_file) is list else [background_asset_upload_file])
        return self
        
    class Include(StringEnum):
        INTERNAL_BETA_RELEASE = 'internalBetaRelease'
        ASSET_FILE = 'assetFile'
        MANIFEST_FILE = 'manifestFile'

    def filter(self, *, state: Union[AppStoreVersionState, list[AppStoreVersionState]]=None, version: Union[str, list[str]]=None, internal_beta_release_state: Union[BetaReviewState, list[BetaReviewState]]=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[AppStoreVersionState, list[AppStoreVersionState]] = None

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :param internal_beta_release_state: filter by attribute 'internalBetaRelease.state'
        :type internal_beta_release_state: Union[BetaReviewState, list[BetaReviewState]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        if internal_beta_release_state: self._set_filter('internalBetaRelease.state', internal_beta_release_state if type(internal_beta_release_state) is list else [internal_beta_release_state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfBackgroundAssetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version: SortOrder=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        return self
        
    def limit(self, number: int=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetVersionsResponse:
        '''Get one or more resources.

        :returns: List of BackgroundAssetVersions
        :rtype: BackgroundAssetVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionsResponse.parse_obj(json)

