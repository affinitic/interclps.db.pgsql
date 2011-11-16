# -*- coding: utf-8 -*-
"""
interclps.db.pgsql

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: baseTypes.py 5772 2011-11-06 15:59:55Z amulux $
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class Province(MappedClassBase):
    c = None


class Commune(MappedClassBase):
    c = None


class MotCle(MappedClassBase):
    c = None


class LinkMotCleTheme(MappedClassBase):
    c = None


class Theme(MappedClassBase):
    c = None


class Public(MappedClassBase):
    c = None


class MilieuDeVie(MappedClassBase):
    c = None


class PlateForme(MappedClassBase):
    c = None


class SousPlateForme(MappedClassBase):
    c = None


class Institution(MappedClassBase):
    c = None


class InstitutionType(MappedClassBase):
    c = None


class InstitutionAssuetudeIntervention(MappedClassBase):
    c = None


class LinkInstitutionAssuetudeIntervention(MappedClassBase):
    c = None


class InstitutionAssuetudeActiviteProposee(MappedClassBase):
    c = None


class LinkInstitutionAssuetudeActiviteProposeePublic(MappedClassBase):
    c = None


class LinkInstitutionAssuetudeActiviteProposeePro(MappedClassBase):
    c = None


class InstitutionAssuetudeThematique(MappedClassBase):
    c = None


class LinkInstitutionAssuetudeThematique(MappedClassBase):
    c = None


class LinkInstitutionCommuneCouverte(MappedClassBase):
    c = None


class LinkInstitutionSousPlateForme(MappedClassBase):
    c = None


class Support(MappedClassBase):
    c = None


class Ressource(MappedClassBase):
    c = None


class Experience(MappedClassBase):
    c = None


class LinkRessourceMotCle(MappedClassBase):
    c = None


class LinkRessourceSupport(MappedClassBase):
    c = None


class LinkRessourceTheme(MappedClassBase):
    c = None


class LinkRessourcePublic(MappedClassBase):
    c = None


class LinkExperienceCommune(MappedClassBase):
    c = None


class LinkExperienceInstitutionPorteur(MappedClassBase):
    c = None


class LinkExperienceInstitutionPartenaire(MappedClassBase):
    c = None


class LinkExperienceInstitutionRessource(MappedClassBase):
    c = None


class LinkExperienceRessource(MappedClassBase):
    c = None


class LinkExperienceMilieuDeVie(MappedClassBase):
    c = None


class LinkExperienceSousPlateForme(MappedClassBase):
    c = None


class LinkExperienceMotCle(MappedClassBase):
    c = None


class LinkExperienceTheme(MappedClassBase):
    c = None


class LinkExperiencePublic(MappedClassBase):
    c = None


class LinkExperienceCommune(MappedClassBase):
    c = None


class Recit(MappedClassBase):
    c = None


class LinkOutilRecit(MappedClassBase):
    c = None


class Auteur(MappedClassBase):
    c = None


class RechercheLog(MappedClassBase):
    c = None
