from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    skyrunner: Skyrunner
    travelata: Travelata
    OnlineTours: OnlineTours
    no: No


class Skyrunner:
    @staticmethod
    def title() -> Literal["""Voyageur céleste"""]: ...

    @staticmethod
    def description() -> Literal["""Un système Web de récupération d’information sur l’aviation qui permet aux utilisateurs de consulter l’information sur les vols selon divers critères."""]: ...


class Travelata:
    @staticmethod
    def title() -> Literal["""Travelata"""]: ...

    @staticmethod
    def description() -> Literal["""Une agence de voyage nouvelle génération. Nous utilisons toute la technologie disponible aujourd’hui pour rendre le choix de voyage, le paiement et la réservation de voyage aussi pratique et agréable que possible pour vous."""]: ...


class OnlineTours:
    @staticmethod
    def title() -> Literal["""Visites en ligne"""]: ...

    @staticmethod
    def description() -> Literal["""RENDRE LE MONDE PLUS PROCHE ET PLUS ACCESSIBLE - Plus de 1000 visites en ligne - Assistance voyage 24/7 - Quick Search Tour - Nous prenons toute l’organisation de la visite."""]: ...


class No:
    @staticmethod
    def copy() -> Literal["""This type of update is not supported by the send_copy method"""]: ...

