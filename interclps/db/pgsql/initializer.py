from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy.orm import mapper, relation, backref
from interclps.db.pgsql.baseTypes import (Province,
                                          Commune,
                                          Clps,
                                          PlateForme,
                                          SousPlateForme,
                                          MotCle,
                                          Theme,
                                          Public,
                                          MilieuDeVie,
                                          Support,
                                          Ressource,
                                          LinkRessourceSupport,
                                          LinkRessourceTheme,
                                          LinkRessourcePublic,
                                          LinkRessourceClpsProprio,
                                          LinkRessourceClpsDispo,
                                          Institution,
                                          InstitutionType,
                                          LinkInstitutionCommuneCouverte,
                                          LinkInstitutionClpsProprio,
                                          LinkInstitutionSousPlateForme,
                                          AssuetudeInterventionForInstitution,
                                          AssuetudeActiviteProposeeForInstitution,
                                          AssuetudeThemeForInstitution,
                                          LinkAssuetudeInterventionForInstitution,
                                          LinkAssuetudeActiviteProposeeForInstitutionPublic,
                                          LinkAssuetudeActiviteProposeeForInstitutionPro,
                                          LinkAssuetudeThemeForInstitution,
                                          Experience,
                                          LinkExperienceInstitutionPorteur,
                                          LinkExperienceInstitutionPartenaire,
                                          LinkExperienceInstitutionRessource,
                                          LinkExperienceRessource,
                                          LinkExperienceMilieuDeVie,
                                          LinkExperienceSousPlateForme,
                                          LinkExperienceMotCle,
                                          LinkExperienceTheme,
                                          LinkExperiencePublic,
                                          LinkExperienceCommune,
                                          LinkExperienceClpsProprio,
                                          Recit,
                                          Auteur,
                                          RechercheLog,
                                          ExperienceMaj)
from interclps.db.pgsql.tables import (getAllProvince,
                                       getAllCommune,
                                       getAllClps,
                                       getAllPlateForme,
                                       getAllSousPlateForme,
                                       getAllMotCle,
                                       getAllTheme,
                                       getAllPublic,
                                       getAllMilieuDeVie,
                                       getAllInstitution,
                                       getAllInstitutionType,
                                       getLinkInstitutionCommuneCouverte,
                                       getLinkInstitutionClpsProprio,
                                       getLinkInstitutionSousPlateForme,
                                       getAllAssuetudeInterventionForInstitution,
                                       getAllAssuetudeActiviteProposeeForInstitution,
                                       getAllAssuetudeThemeForInstitution,
                                       getLinkAssuetudeInterventionForInstitution,
                                       getLinkAssuetudeActiviteProposeeForInstitutionPublic,
                                       getLinkAssuetudeActiviteProposeeForInstitutionPro,
                                       getLinkAssuetudeThemeForInstitution,
                                       getAllSupport,
                                       getAllRessource,
                                       getLinkRessourceSupport,
                                       getLinkRessourceTheme,
                                       getLinkRessourcePublic,
                                       getLinkRessourceClpsProprio,
                                       getLinkRessourceClpsDispo,
                                       getAllRecit,
                                       getAllExperience,
                                       getLinkExperienceInstitutionPorteur,
                                       getLinkExperienceInstitutionPartenaire,
                                       getLinkExperienceInstitutionRessource,
                                       getLinkExperienceRessource,
                                       getLinkExperienceMilieuDeVie,
                                       getLinkExperienceSousPlateForme,
                                       getLinkExperienceMotCle,
                                       getLinkExperienceTheme,
                                       getLinkExperiencePublic,
                                       getLinkExperienceCommune,
                                       getLinkExperienceClpsProprio,
                                       getAllAuteur,
                                       getAllRechercheLog,
                                       getAllExperienceMaj)


class InterClpsModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
            table de demo employe
        """
        model = Model()
        model.metadata = metadata

## table province ##
        provinceTable = getAllProvince(metadata)
        provinceTable.create(checkfirst=True)
        mapper(Province, provinceTable)
        model.add('province', table=provinceTable, mapper_class=Province)

## table commune ##
        communeTable = getAllCommune(metadata)
        communeTable.create(checkfirst=True)
        mapper(Commune, communeTable,
               properties={'province': relation(Province,
                                                uselist=False,
                                                backref=backref('commune',
                                                                lazy=True,
                                                                uselist=False))})
        model.add('commune', table=communeTable, mapper_class=Commune)

## table clps ##
        clpsTable = getAllClps(metadata)
        clpsTable.create(checkfirst=True)
        mapper(Clps, clpsTable,
               properties={'commune': relation(Commune,
                                               uselist=False)})
        model.add('clps',
                  table=clpsTable,
                  mapper_class=Clps)

## table plateforme ##
        plateformeTable = getAllPlateForme(metadata)
        plateformeTable.create(checkfirst=True)
        mapper(PlateForme, plateformeTable)
        model.add('plateforme', table=plateformeTable, mapper_class=PlateForme)

## table sous_plateforme ##
        sousplateformeTable = getAllSousPlateForme(metadata)
        sousplateformeTable.create(checkfirst=True)
        mapper(SousPlateForme, sousplateformeTable,
               properties={'plateforme': relation(PlateForme,
                                                  uselist=False,
                                                  backref=backref('sousplateforme',
                                                                  lazy=True,
                                                                  uselist=False))})
        model.add('sousplateforme', table=sousplateformeTable, mapper_class=SousPlateForme)

## table public ##
        publicTable = getAllPublic(metadata)
        publicTable.create(checkfirst=True)
        mapper(Public, publicTable)
        model.add('public', table=publicTable, mapper_class=Public)

## table milieu de vie ##
        milieuDeVieTable = getAllMilieuDeVie(metadata)
        milieuDeVieTable.create(checkfirst=True)
        mapper(MilieuDeVie, milieuDeVieTable)
        model.add('milieudevie', table=milieuDeVieTable, mapper_class=MilieuDeVie)

## table theme ##
        themeTable = getAllTheme(metadata)
        themeTable.create(checkfirst=True)
        mapper(Theme, themeTable)
        model.add('theme', table=themeTable, mapper_class=Theme)

## table motcle ##
        motCleTable = getAllMotCle(metadata)
        motCleTable.create(checkfirst=True)
        mapper(MotCle, motCleTable)
        model.add('motcle',
                  table=motCleTable,
                  mapper_class=MotCle)

## table auteur  ##
        auteurTable = getAllAuteur(metadata)
        auteurTable.create(checkfirst=True)
        mapper(Auteur, auteurTable,
               properties={'experienceFromAuteur': relation(Experience,
                                                            uselist=False,
                                                            backref=backref('auteurFromExperience',
                                                                            lazy=True,
                                                                            uselist=False)),
                           'clpsOrigine': relation(Clps,
                                                   uselist=False)})
        model.add('auteur',
                  table=auteurTable,
                  mapper_class=Auteur)

## table institution-type ##
        institutionTypeTable = getAllInstitutionType(metadata)
        institutionTypeTable.create(checkfirst=True)
        mapper(InstitutionType, institutionTypeTable)
        model.add('institution_type', table=institutionTypeTable, mapper_class=InstitutionType)

## table institution ##
        institutionTable = getAllInstitution(metadata)
        institutionTable.create(checkfirst=True)
        mapper(Institution, institutionTable,
               properties={'commune': relation(Commune,
                                               uselist=False,
                                               backref=backref('institution',
                                                               lazy=True,
                                                               uselist=False)),
                           'auteur': relation(Auteur,
                                              uselist=False),
                           'type': relation(InstitutionType,
                                            uselist=False)})
        model.add('institution', table=institutionTable, mapper_class=Institution)

        LinkInstitutionSousPlateFormeTable = getLinkInstitutionSousPlateForme(metadata)
        LinkInstitutionSousPlateFormeTable.create(checkfirst=True)
        mapper(LinkInstitutionSousPlateForme, LinkInstitutionSousPlateFormeTable)
        model.add('link_institution_sousplateforme',
                  table=LinkInstitutionSousPlateFormeTable,
                  mapper_class=LinkInstitutionSousPlateForme)

        linkInstitutionCommuneCouverteTable = getLinkInstitutionCommuneCouverte(metadata)
        linkInstitutionCommuneCouverteTable.create(checkfirst=True)
        mapper(LinkInstitutionCommuneCouverte, linkInstitutionCommuneCouverteTable,
               primary_key=[linkInstitutionCommuneCouverteTable.c.institution_fk, linkInstitutionCommuneCouverteTable.c.commune_fk])
        model.add('link_institution_commune_couverte',
                  table=linkInstitutionCommuneCouverteTable,
                  mapper_class=LinkInstitutionCommuneCouverte)

        LinkInstitutionClpsProprioTable = getLinkInstitutionClpsProprio(metadata)
        LinkInstitutionClpsProprioTable.create(checkfirst=True)
        mapper(LinkInstitutionClpsProprio, LinkInstitutionClpsProprioTable)
        model.add('link_institution_clps_proprio',
                  table=LinkInstitutionClpsProprioTable,
                  mapper_class=LinkInstitutionClpsProprio)

## table info assuetude pour institution ##
        AssuetudeInterventionForInstitutionTable = getAllAssuetudeInterventionForInstitution(metadata)
        AssuetudeInterventionForInstitutionTable.create(checkfirst=True)
        mapper(AssuetudeInterventionForInstitution, AssuetudeInterventionForInstitutionTable)
        model.add('assuetude_intervention_for_institution', table=AssuetudeInterventionForInstitutionTable, mapper_class=AssuetudeInterventionForInstitution)

        linkAssuetudeInterventionForInstitutionTable = getLinkAssuetudeInterventionForInstitution(metadata)
        linkAssuetudeInterventionForInstitutionTable.create(checkfirst=True)
        mapper(LinkAssuetudeInterventionForInstitution, linkAssuetudeInterventionForInstitutionTable,
               primary_key=[linkAssuetudeInterventionForInstitutionTable.c.institution_fk, linkAssuetudeInterventionForInstitutionTable.c.assuetude_intervention_fk],
               properties={'assuetudeIntervention': relation(AssuetudeInterventionForInstitution,
                                                             uselist=False)})
        model.add('link_institution_asuetude_intervention',
                  table=linkAssuetudeInterventionForInstitutionTable,
                  mapper_class=LinkAssuetudeInterventionForInstitution)

        assuetudeActiviteProposeeForInstitutionTable = getAllAssuetudeActiviteProposeeForInstitution(metadata)
        assuetudeActiviteProposeeForInstitutionTable.create(checkfirst=True)
        mapper(AssuetudeActiviteProposeeForInstitution, assuetudeActiviteProposeeForInstitutionTable)
        model.add('assuetude_activite_proposee_for_institution',
                  table=assuetudeActiviteProposeeForInstitutionTable,
                  mapper_class=AssuetudeActiviteProposeeForInstitution)

        linkAssuetudeActiviteProposeePublicForInstitutionTable = getLinkAssuetudeActiviteProposeeForInstitutionPublic(metadata)
        linkAssuetudeActiviteProposeePublicForInstitutionTable.create(checkfirst=True)
        mapper(LinkAssuetudeActiviteProposeeForInstitutionPublic, linkAssuetudeActiviteProposeePublicForInstitutionTable,
               primary_key=[linkAssuetudeActiviteProposeePublicForInstitutionTable.c.institution_fk, linkAssuetudeActiviteProposeePublicForInstitutionTable.c.assuetude_activite_proposee_public_fk])
        model.add('link_institution_asuetude_activite_proposee_public',
                  table=linkAssuetudeActiviteProposeePublicForInstitutionTable,
                  mapper_class=LinkAssuetudeActiviteProposeeForInstitutionPublic)

        linkAssuetudeActiviteProposeeProForInstitutionTable = getLinkAssuetudeActiviteProposeeForInstitutionPro(metadata)
        linkAssuetudeActiviteProposeeProForInstitutionTable.create(checkfirst=True)
        mapper(LinkAssuetudeActiviteProposeeForInstitutionPro, linkAssuetudeActiviteProposeeProForInstitutionTable,
               primary_key=[linkAssuetudeActiviteProposeeProForInstitutionTable.c.institution_fk, linkAssuetudeActiviteProposeeProForInstitutionTable.c.assuetude_activite_proposee_pro_fk])
        model.add('link_institution_asuetude_activite_proposee_pro',
                  table=linkAssuetudeActiviteProposeeProForInstitutionTable,
                  mapper_class=LinkAssuetudeActiviteProposeeForInstitutionPro)

        assuetudeThematiqueForInstitutionTable = getAllAssuetudeThemeForInstitution(metadata)
        assuetudeThematiqueForInstitutionTable.create(checkfirst=True)
        mapper(AssuetudeThemeForInstitution, assuetudeThematiqueForInstitutionTable)
        model.add('assuetude_thematique_for_institution',
                  table=assuetudeThematiqueForInstitutionTable,
                  mapper_class=AssuetudeThemeForInstitution)

        linkAssuetudeThemeForInstitutionTable = getLinkAssuetudeThemeForInstitution(metadata)
        linkAssuetudeThemeForInstitutionTable.create(checkfirst=True)
        mapper(LinkAssuetudeThemeForInstitution, linkAssuetudeThemeForInstitutionTable,
               primary_key=[linkAssuetudeThemeForInstitutionTable.c.institution_fk, linkAssuetudeThemeForInstitutionTable.c.assuetude_thematique_fk])
        model.add('link_institution_assuetude_thematique',
                  table=linkAssuetudeThemeForInstitutionTable,
                  mapper_class=LinkAssuetudeThemeForInstitution)

## table support ##
        supportTable = getAllSupport(metadata)
        supportTable.create(checkfirst=True)
        mapper(Support, supportTable)
        model.add('support', table=supportTable, mapper_class=Support)

## table ressource liee a la table support et a la table theme ##
        ressourceTable = getAllRessource(metadata)
        ressourceTable.create(checkfirst=True)
        mapper(Ressource, ressourceTable)
        model.add('ressource', table=ressourceTable, mapper_class=Ressource)

        LinkRessourceSupportTable = getLinkRessourceSupport(metadata)
        LinkRessourceSupportTable.create(checkfirst=True)
        mapper(LinkRessourceSupport, LinkRessourceSupportTable)
        model.add('link_ressource_support',
                  table=LinkRessourceSupportTable,
                  mapper_class=LinkRessourceSupport)

        LinkRessourceThemeTable = getLinkRessourceTheme(metadata)
        LinkRessourceThemeTable.create(checkfirst=True)
        mapper(LinkRessourceTheme, LinkRessourceThemeTable)
        model.add('link_ressource_theme',
                  table=LinkRessourceThemeTable,
                  mapper_class=LinkRessourceTheme)

        LinkRessourcePublicTable = getLinkRessourcePublic(metadata)
        LinkRessourcePublicTable.create(checkfirst=True)
        mapper(LinkRessourcePublic, LinkRessourcePublicTable)
        model.add('link_ressource_public',
                  table=LinkRessourcePublicTable,
                  mapper_class=LinkRessourcePublic)

        LinkRessourceClpsProprioTable = getLinkRessourceClpsProprio(metadata)
        LinkRessourceClpsProprioTable.create(checkfirst=True)
        mapper(LinkRessourceClpsProprio, LinkRessourceClpsProprioTable,
               properties={'ressourceOfClpsProprio': relation(Ressource, lazy=True),
                           'proprio': relation(Clps, lazy=True)})
        model.add('link_ressource_clps_proprio',
                  table=LinkRessourceClpsProprioTable,
                  mapper_class=LinkRessourceClpsProprio)

        LinkRessourceClpsDispoTable = getLinkRessourceClpsDispo(metadata)
        LinkRessourceClpsDispoTable.create(checkfirst=True)
        mapper(LinkRessourceClpsDispo, LinkRessourceClpsDispoTable)
        model.add('link_ressource_clps_dispo',
                  table=LinkRessourceClpsDispoTable,
                  mapper_class=LinkRessourceClpsDispo)

## table recit ##
        recitTable = getAllRecit(metadata)
        recitTable.create(checkfirst=True)
        mapper(Recit, recitTable)
        model.add('recit', table=recitTable, mapper_class=Recit)

## table experience ##
        LinkExperienceInstitutionPorteurTable = getLinkExperienceInstitutionPorteur(metadata)
        LinkExperienceInstitutionPorteurTable.create(checkfirst=True)
        mapper(LinkExperienceInstitutionPorteur, LinkExperienceInstitutionPorteurTable,
               properties={'institution_porteur': relation(Institution, lazy=True)})
        model.add('link_experience_institution_porteur',
                  table=LinkExperienceInstitutionPorteurTable,
                  mapper_class=LinkExperienceInstitutionPorteur)

        LinkExperienceInstitutionPartenaireTable = getLinkExperienceInstitutionPartenaire(metadata)
        LinkExperienceInstitutionPartenaireTable.create(checkfirst=True)
        mapper(LinkExperienceInstitutionPartenaire, LinkExperienceInstitutionPartenaireTable,
               properties={'institution_partenaire': relation(Institution, lazy=True)})
        model.add('link_experience_institution_partenaire',
                  table=LinkExperienceInstitutionPartenaireTable,
                  mapper_class=LinkExperienceInstitutionPartenaire)

        LinkExperienceInstitutionRessourceTable = getLinkExperienceInstitutionRessource(metadata)
        LinkExperienceInstitutionRessourceTable.create(checkfirst=True)
        mapper(LinkExperienceInstitutionRessource, LinkExperienceInstitutionRessourceTable,
               properties={'institution_ressource': relation(Institution, lazy=True)})
        model.add('link_experience_institution_ressource',
                  table=LinkExperienceInstitutionRessourceTable,
                  mapper_class=LinkExperienceInstitutionRessource)

        LinkExperienceClpsProprioTable = getLinkExperienceClpsProprio(metadata)
        LinkExperienceClpsProprioTable.create(checkfirst=True)
        mapper(LinkExperienceClpsProprio, LinkExperienceClpsProprioTable)
        model.add('link_experience_clps_proprio',
                  table=LinkExperienceClpsProprioTable,
                  mapper_class=LinkExperienceClpsProprio)

        LinkExperienceRessourceTable = getLinkExperienceRessource(metadata)
        LinkExperienceRessourceTable.create(checkfirst=True)
        mapper(LinkExperienceRessource, LinkExperienceRessourceTable)
        model.add('link_experience_ressource',
                  table=LinkExperienceRessourceTable,
                  mapper_class=LinkExperienceRessource)

        LinkExperienceMilieuDeVieTable = getLinkExperienceMilieuDeVie(metadata)
        LinkExperienceMilieuDeVieTable.create(checkfirst=True)
        mapper(LinkExperienceMilieuDeVie, LinkExperienceMilieuDeVieTable)
        model.add('link_experience_milieudevie',
                  table=LinkExperienceMilieuDeVieTable,
                  mapper_class=LinkExperienceMilieuDeVie)

        LinkExperienceSousPlateFormeTable = getLinkExperienceSousPlateForme(metadata)
        LinkExperienceSousPlateFormeTable.create(checkfirst=True)
        mapper(LinkExperienceSousPlateForme, LinkExperienceSousPlateFormeTable)
        model.add('link_experience_sousplateforme',
                  table=LinkExperienceSousPlateFormeTable,
                  mapper_class=LinkExperienceSousPlateForme)

        LinkExperienceMotCleTable = getLinkExperienceMotCle(metadata)
        LinkExperienceMotCleTable.create(checkfirst=True)
        mapper(LinkExperienceMotCle, LinkExperienceMotCleTable)
        model.add('link_experience_mot_cle',
                  table=LinkExperienceMotCleTable,
                  mapper_class=LinkExperienceMotCle)

        LinkExperienceThemeTable = getLinkExperienceTheme(metadata)
        LinkExperienceThemeTable.create(checkfirst=True)
        mapper(LinkExperienceTheme, LinkExperienceThemeTable)
        model.add('link_experience_theme',
                  table=LinkExperienceThemeTable,
                  mapper_class=LinkExperienceTheme)

        LinkExperiencePublicTable = getLinkExperiencePublic(metadata)
        LinkExperiencePublicTable.create(checkfirst=True)
        mapper(LinkExperiencePublic, LinkExperiencePublicTable)
        model.add('link_experience_public',
                  table=LinkExperiencePublicTable,
                  mapper_class=LinkExperiencePublic)

        LinkExperienceCommuneTable = getLinkExperienceCommune(metadata)
        LinkExperienceCommuneTable.create(checkfirst=True)
        mapper(LinkExperienceCommune, LinkExperienceCommuneTable)
        model.add('link_experience_commune',
                  table=LinkExperienceCommuneTable,
                  mapper_class=LinkExperienceCommune)


        experienceTable = getAllExperience(metadata)
        experienceTable.create(checkfirst=True)
        mapper(Experience, experienceTable,
               properties={'institution_porteur': relation(LinkExperienceInstitutionPorteur, lazy=True),
                           'institution_partenaire': relation(LinkExperienceInstitutionPartenaire, lazy=True),
                           'clpsOrigine': relation(Clps,
                                                   uselist=False)})
                           #'institution_ressource': relation(LinkExperienceInstitutionRessource, lazy=True),
                           #'ressource': relation(LinkExperienceRessource, lazy=True)

        model.add('experience',
                  table=experienceTable,
                  mapper_class=Experience)

## table experiencemaj > versionning ##
        experienceMajTable = getAllExperienceMaj(metadata)
        experienceMajTable.create(checkfirst=True)
        mapper(ExperienceMaj, experienceMajTable,
               properties={'clps_proprio': relation(Clps, uselist=False)})
        model.add('experience_maj',
                  table=experienceMajTable,
                  mapper_class=ExperienceMaj)

## table rechercheLog ##
        rechercheLogTable = getAllRechercheLog(metadata)
        rechercheLogTable.create(checkfirst=True)
        mapper(RechercheLog, rechercheLogTable)
        model.add('rechercheLog', table=rechercheLogTable, mapper_class=Recit)

        metadata.create_all()
        return model
