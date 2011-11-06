# -*- coding: utf-8 -*-
"""
interclps.db.pgsql

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: baseTypes.py 5772 2011-11-06 15:59:55Z amulux $
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class Province(MappedClassBase):
    pass


class Commune(MappedClassBase):
    pass


class MotCle(MappedClassBase):
    pass


class LinkMotCleTheme(MappedClassBase):
    pass


class Theme(MappedClassBase):
    pass


class Public(MappedClassBase):
    pass


class MilieuDeVie(MappedClassBase):
    pass


class PlateForme(MappedClassBase):
    pass


class SousPlateForme(MappedClassBase):
    pass


class Institution(MappedClassBase):
    pass


class InstitutionType(MappedClassBase):
    pass


class InstitutionAssuetudeIntervention(MappedClassBase):
    pass


class LinkInstitutionAssuetudeIntervention(MappedClassBase):
    pass


class InstitutionAssuetudeActiviteProposee(MappedClassBase):
    pass


class LinkInstitutionAssuetudeActiviteProposeePublic(MappedClassBase):
    pass


class LinkInstitutionAssuetudeActiviteProposeePro(MappedClassBase):
    pass


class InstitutionAssuetudeThematique(MappedClassBase):
    pass


class LinkInstitutionAssuetudeThematique(MappedClassBase):
    pass


class LinkInstitutionCommuneCouverte(MappedClassBase):
    pass


class LinkInstitutionSousPlateForme(MappedClassBase):
    pass


class Support(MappedClassBase):
    pass


class Ressource(MappedClassBase):
    pass


class Experience(MappedClassBase):
    pass


class LinkRessourceMotCle(MappedClassBase):
    pass


class LinkRessourceSupport(MappedClassBase):
    pass


class LinkRessourceTheme(MappedClassBase):
    pass


class LinkRessourcePublic(MappedClassBase):
    pass


class LinkExperienceCommune(MappedClassBase):
    pass


class LinkExperienceInstitutionPorteur(MappedClassBase):
    pass


class LinkExperienceInstitutionPartenaire(MappedClassBase):
    pass


class LinkExperienceInstitutionRessource(MappedClassBase):
    pass


class LinkExperienceRessource(MappedClassBase):
    pass


class LinkExperienceMilieuDeVie(MappedClassBase):
    pass


class LinkExperienceSousPlateForme(MappedClassBase):
    pass


class LinkExperienceMotCle(MappedClassBase):
    pass


class LinkExperienceTheme(MappedClassBase):
    pass


class LinkExperiencePublic(MappedClassBase):
    pass


class LinkExperienceCommune(MappedClassBase):
    pass


class Recit(MappedClassBase):
    pass


class LinkOutilRecit(MappedClassBase):
    pass


class Auteur(MappedClassBase):
    pass


class RechercheLog(MappedClassBase):
    pass
