from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardLocalizations'

    def create(self, request: GameCenterLeaderboardLocalizationCreateRequest) -> GameCenterLeaderboardLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardLocalization representation
        :type request: GameCenterLeaderboardLocalizationCreateRequest

        :returns: Single GameCenterLeaderboardLocalization
        :rtype: GameCenterLeaderboardLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardLocalizationResponse.parse_obj(json)

class GameCenterLeaderboardLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardLocalizations/{id}'

    @endpoint('/v1/gameCenterLeaderboardLocalizations/{id}/gameCenterLeaderboardImage')
    def game_center_leaderboard_image(self) -> GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint:
        return GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage')
    def game_center_leaderboard_image_linkage(self) -> GameCenterLeaderboardImageLinkageOfGameCenterLeaderboardLocalizationEndpoint:
        return GameCenterLeaderboardImageLinkageOfGameCenterLeaderboardLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None) -> GameCenterLeaderboardLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardLocalizationEndpoint
        '''
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'
        GAME_CENTER_LEADERBOARD_IMAGE = 'gameCenterLeaderboardImage'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterLeaderboardLocalizationResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardLocalization
        :rtype: GameCenterLeaderboardLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardLocalizationResponse.parse_obj(json)

    def update(self, request: GameCenterLeaderboardLocalizationUpdateRequest) -> GameCenterLeaderboardLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardLocalization representation
        :type request: GameCenterLeaderboardLocalizationUpdateRequest

        :returns: Single GameCenterLeaderboardLocalization
        :rtype: GameCenterLeaderboardLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardImageLinkageOfGameCenterLeaderboardLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage'

    def get(self) -> GameCenterLeaderboardLocalizationGameCenterLeaderboardImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardLocalizationGameCenterLeaderboardImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardLocalizationGameCenterLeaderboardImageLinkageResponse.parse_obj(json)

class GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardLocalizations/{id}/gameCenterLeaderboardImage'

    def fields(self, *, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None) -> GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint
        '''
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_LOCALIZATION = 'gameCenterLeaderboardLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageOfGameCenterLeaderboardLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterLeaderboardImageResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardImageResponse.parse_obj(json)

