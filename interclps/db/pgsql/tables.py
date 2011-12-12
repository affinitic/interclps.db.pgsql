# -*- coding: utf-8 -*-

from sqlalchemy import (Table, Column, ForeignKey, Integer, Text, Sequence, func, DateTime, Boolean)


def getAllProvince(metadata):
    autoload = False
    if metadata.bind.has_table('province'):
        autoload = True
    province = Table('province', metadata,
                    Column('prov_pk', Integer(),
                           Sequence('province_prov_pk_seq'),
                           primary_key = True),
                    Column('prov_nom', Text()),
                    autoload=autoload,
                    useexisting=True)
    return province


def getAllCommune(metadata):
    autoload = False
    if metadata.bind.has_table('commune'):
        autoload = True
    commune = Table('commune', metadata,
                    Column('com_pk', Integer(),
                           Sequence('commune_com_pk_seq'),
                           primary_key = True),
                    Column('com_localite_cp', Text()),
                    Column('com_localite_nom', Text()),
                    Column('com_commune_cp', Text()),
                    Column('com_commune_nom', Text()),
                    Column('com_commune_langue', Text()),
                    Column('com_province_fk', Integer(),
                           ForeignKey('province.prov_pk'),
                           nullable=False),
                    autoload=autoload,
                    useexisting=True)
    return commune


def getAllClps(metadata):
    autoload = False
    if metadata.bind.has_table('clps'):
        autoload = True
    clps = Table('clps', metadata,
                 Column('clps_pk', Integer(),
                        Sequence('clps_clps_pk_seq', optional=True),
                        primary_key = True),
                 Column('clps_nom', Text()),
                 autoload=autoload)
    return clps


def getAllPlateForme(metadata):
    autoload = False
    if metadata.bind.has_table('plateforme'):
        autoload = True
    plateforme = Table('plateforme', metadata,
                       Column('plateforme_pk', Integer(),
                              Sequence('plateforme_plateforme_pk_seq'),
                              primary_key = True),
                      Column('plateforme_nom', Text()),
                      Column('plateforme_actif', Boolean()),
                      Column('plateforme_creation_date', DateTime(), default = func.now()),
                      Column('plateforme_modification_date', DateTime()),
                      Column('plateforme_modification_employe', Text()),
                      autoload=autoload,
                      useexisting=True)
    return plateforme


def getAllSousPlateForme(metadata):
    autoload = False
    if metadata.bind.has_table('sousplateforme'):
        autoload = True
    sousplateforme = Table('sousplateforme', metadata,
                            Column('sousplateforme_pk', Integer(),
                                   Sequence('sousplateforme_sousplateforme_pk_seq'),
                                   primary_key = True),
                            Column('sousplateforme_nom', Text()),
                            Column('sousplateforme_actif', Boolean()),
                            Column('sousplateforme_creation_date', DateTime(), default = func.now()),
                            Column('sousplateforme_modification_date', DateTime()),
                            Column('sousplateforme_modification_employe', Text()),
                            Column('sousplateforme_plateforme_fk', Integer(),
                                   ForeignKey('plateforme.plateforme_pk'),
                                   nullable=False),
                            autoload=autoload,
                            useexisting=True)
    return sousplateforme


def getAllMotCle(metadata):
    autoload = False
    if metadata.bind.has_table('mot_cle'):
        autoload = True
    motCle = Table('mot_cle', metadata,
                    Column('motcle_pk', Integer(),
                           Sequence('mot_cle_motcle_pk_seq'),
                           primary_key = True),
                    Column('motcle_mot', Text()),
                    Column('motcle_actif', Boolean()),
                    Column('motcle_creation_date', DateTime(), default = func.now()),
                    Column('motcle_modification_date', DateTime()),
                    Column('motcle_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return motCle


def getAllTheme(metadata):
    autoload = False
    if metadata.bind.has_table('theme'):
        autoload = True
    theme = Table('theme', metadata,
                    Column('theme_pk', Integer(),
                           Sequence('theme_theme_pk_seq'),
                           primary_key = True),
                    Column('theme_nom', Text()),
                    Column('theme_actif', Boolean()),
                    Column('theme_creation_date', DateTime(), default = func.now()),
                    Column('theme_modification_date', DateTime()),
                    Column('theme_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return theme


def getAllPublic(metadata):
    autoload = False
    if metadata.bind.has_table('public'):
        autoload = True
    public = Table('public', metadata,
                    Column('public_pk', Integer(),
                           Sequence('public_public_pk_seq'),
                           primary_key = True),
                    Column('public_nom', Text()),
                    Column('public_actif', Boolean()),
                    Column('public_creation_date', DateTime(), default = func.now()),
                    Column('public_modification_date', DateTime()),
                    Column('public_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return public


def getAllMilieuDeVie(metadata):
    autoload = False
    if metadata.bind.has_table('milieudevie'):
        autoload = True
    milieudevie = Table('milieudevie', metadata,
                    Column('milieudevie_pk', Integer(),
                           Sequence('milieudevie_milieudevie_pk_seq'),
                           primary_key = True),
                    Column('milieudevie_nom', Text()),
                    Column('milieudevie_actif', Boolean()),
                    Column('milieudevie_creation_date', DateTime(), default = func.now()),
                    Column('milieudevie_modification_date', DateTime()),
                    Column('milieudevie_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return milieudevie


def getAllInstitution(metadata):
    autoload = False
    if metadata.bind.has_table('institution'):
        autoload = True
    institution = Table('institution', metadata,
                        Column('institution_pk', Integer(),
                               Sequence('institution_institution_pk_seq'),
                               primary_key = True),
                        Column('institution_nom', Text()),
                        Column('institution_sigle', Text()),
                        Column('institution_adresse', Text()),
                        Column('institution_nom_contact', Text()),
                        Column('institution_email_contact', Text()),
                        Column('institution_tel_contact', Text()),
                        Column('institution_fonction_contact', Text()),
                        Column('institution_url_site', Text()),
                        Column('institution_lien_siss', Text()),
                        Column('institution_lien_autre', Text()),
                        Column('institution_autre_info', Text()),
                        Column('institution_mission', Text()),
                        Column('institution_activite', Text()),
                        Column('institution_public', Text()),
                        Column('institution_etat', Text()),
                        Column('institution_creation_date', DateTime()),
                        Column('institution_modification_date', DateTime(), default = func.now()),
                        Column('institution_modification_employe', Text()),
                        Column('institution_territoire_tout_brabant_wallon', Boolean()),
                        Column('institution_zone_internationale', Boolean()),
                        Column('institution_zone_internationale_info', Text()),
                        Column('institution_zone_belgique', Boolean()),
                        Column('institution_zone_cfwb', Boolean()),
                        Column('institution_zone_rw', Boolean()),
                        Column('institution_zone_brxl', Boolean()),
                        Column('institution_commentaire', Text()),
                        Column('institution_assuet_intervention', Text()),
                        Column('institution_assuet_intervention_precision', Text()),
                        Column('institution_assuet_activite_proposee', Text()),
                        Column('institution_assuet_activite_proposee_precision', Text()),
                        Column('institution_assuet_thematique_precision', Text()),
                        Column('institution_assuet_aide_soutien_ecole', Text()),
                        Column('institution_plate_forme_sante_ecole', Boolean()),
                        Column('institution_plate_forme_assuetude', Boolean()),
                        Column('institution_plate_forme_sante_famille', Boolean()),
                        Column('institution_plate_forme_sante_environnement', Boolean()),
                        Column('institution_listing_ressource_plate_forme_sante_ecole', Boolean()),
                        Column('institution_listing_ressource_plate_forme_assuetude', Boolean()),
                        Column('institution_listing_ressource_plate_forme_sante_famille', Boolean()),
                        Column('institution_listing_ressource_plate_forme_sante_environnement', Boolean()),
                        Column('institution_auteur_login', Text()),
                        Column('institution_institution_type_fk', Integer(),
                           ForeignKey('institution_type.institution_type_pk'),
                           nullable=False),
                        Column('institution_commune_fk', Integer(),
                           ForeignKey('commune.com_pk'),
                           nullable=False),
                        Column('institution_auteur_fk', Integer(),
                           ForeignKey('auteur.auteur_pk'),
                           nullable=False),
                        autoload=autoload,
                        useexisting=True)
    return institution


def getAllInstitutionType(metadata):
    autoload = False
    if metadata.bind.has_table('institution_type'):
        autoload = True
    institutionType =Table('institution_type', metadata,
                            Column('institution_type_pk', Integer(),
                                   Sequence('institution_type_pk_seq'),
                                   primary_key = True),
                            Column('institution_type_nom', Text()),
                            Column('institution_type_actif', Boolean()),
                            Column('institution_type_creation_date', DateTime()),
                            Column('institution_type_modification_date', DateTime(), default = func.now()),
                            Column('institution_type_modification_employe', Text()),
                            useexisting=True,
                            autoload=autoload)
    return institutionType


def getAllAssuetudeInterventionForInstitution(metadata):
    autoload = False
    if metadata.bind.has_table('assuetude_intervention_for_institution'):
        autoload = True
    assuetudeInterventionForInstitution =Table('assuetude_intervention_for_institution', metadata,
                                               Column('assuetude_intervention_pk', Integer(),
                                                       Sequence('assuetude_intervention_pk_seq'),
                                                       primary_key = True),
                                               Column('assuetude_intervention_nom', Text()),
                                               Column('assuetude_intervention_actif', Boolean(), default = True),
                                               Column('assuetude_intervention_actif', Boolean(), default = True),
                                               Column('assuetude_intervention_num_ordre', Integer(), default = 0),
                                               Column('assuetude_intervention_creation_date', DateTime()),
                                               Column('assuetude_intervention_modification_date', DateTime(), default = func.now()),
                                               Column('assuetude_intervention_modification_employe', Text()),
                                               useexisting=True,
                                               autoload=autoload)
    return assuetudeInterventionForInstitution


def getLinkInstitutionAssuetudeIntervention(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_assuetude_intervention'):
        autoload = True
    linkInstitutionAssuetudeIntervention = Table('link_institution_assuetude_intervention', metadata,
                                                  Column('institution_fk', Integer(),
                                                          ForeignKey('institution.institution_pk'),
                                                          primary_key = True),
                                                  Column('assuetude_intervention_fk', Integer(),
                                                          ForeignKey('assuetude_intervention_for_institution.assuetude_intervention_pk'),
                                                          primary_key = True),
                                                  useexisting=True,
                                                  autoload=autoload)
    return linkInstitutionAssuetudeIntervention


def getAllAssuetudeActiviteProposeeForInstitution(metadata):
    autoload = False
    if metadata.bind.has_table('assuetude_activite_proposee_for_institution'):
        autoload = True
    assuetudeActiviteProposeeForInstitution =Table('assuetude_activite_proposee_for_institution', metadata,
                                                   Column('assuetude_activite_proposee_pk', Integer(),
                                                          Sequence('assuetude_activite_proposee_pk_seq'),
                                                          primary_key = True),
                                                   Column('assuetude_activite_proposee_nom', Text()),
                                                   Column('assuetude_activite_proposee_actif', Boolean(), default = True),
                                                   Column('assuetude_activite_proposee_num_ordre', Integer(), default = 0),
                                                   Column('assuetude_activite_proposee_public', Boolean(), default = True),
                                                   Column('assuetude_activite_proposee_pro', Boolean(), default = True),
                                                   Column('assuetude_activite_proposee_creation_date', DateTime()),
                                                   Column('assuetude_activite_proposee_modification_date', DateTime(), default = func.now()),
                                                   Column('assuetude_activite_proposee_modification_employe', Text()),
                                                   useexisting=True,
                                                   autoload=autoload)
    return assuetudeActiviteProposeeForInstitution


def getLinkInstitutionAssuetudeActiviteProposeePublic(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_assuetude_activite_proposee_public'):
        autoload = True
    linkInstitutionAssuetudeActiviteProposeePublic = Table('link_institution_assuetude_activite_proposee_public', metadata,
                                                     Column('institution_fk', Integer(),
                                                            ForeignKey('institution.institution_pk'),
                                                            primary_key = True),
                                                     Column('assuetude_activite_proposee_public_fk', Integer(),
                                                            ForeignKey('assuetude_activite_proposee_for_institution.assuetude_activite_proposee_pk'),
                                                            primary_key = True),
                                                     useexisting=True,
                                                     autoload=autoload)
    return linkInstitutionAssuetudeActiviteProposeePublic


def getLinkInstitutionAssuetudeActiviteProposeePro(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_assuetude_activite_proposee_pro'):
        autoload = True
    linkInstitutionAssuetudeActiviteProposeePro = Table('link_institution_assuetude_activite_proposee_pro', metadata,
                                                     Column('institution_fk', Integer(),
                                                            ForeignKey('institution.institution_pk'),
                                                            primary_key = True),
                                                     Column('assuetude_activite_proposee_pro_fk', Integer(),
                                                            ForeignKey('assuetude_activite_proposee_for_institution.assuetude_activite_proposee_pk'),
                                                            primary_key = True),
                                                     useexisting=True,
                                                     autoload=autoload)
    return linkInstitutionAssuetudeActiviteProposeePro


def getAllAssuetudeThematiqueForInstitution(metadata):
    autoload = False
    if metadata.bind.has_table('assuetude_thematique_for_institution'):
        autoload = True
    assuetudeThematiqueForInstitution =Table('assuetude_thematique_for_institution', metadata,
                                             Column('assuetude_thematique_pk', Integer(),
                                                     Sequence('assuetude_thematique_for_institution_pk_seq'),
                                                     primary_key = True),
                                             Column('assuetude_thematique_nom', Text()),
                                             Column('assuetude_thematique_actif', Boolean(), default = True),
                                             Column('assuetude_thematique_num_ordre', Integer(), default = 0),
                                             Column('assuetude_thematique_creation_date', DateTime()),
                                             Column('assuetude_thematique_modification_date', DateTime(), default = func.now()),
                                             Column('assuetude_thematique_modification_employe', Text()),
                                             useexisting=True,
                                             autoload=autoload)
    return assuetudeThematiqueForInstitution


def getLinkInstitutionAssuetudeThematique(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_assuetude_thematique'):
        autoload = True
    linkInstitutionAssuetudeThematique = Table('link_institution_assuetude_thematique', metadata,
                                            Column('institution_fk', Integer(),
                                                   ForeignKey('institution.institution_pk'),
                                                   primary_key = True),
                                            Column('assuetude_thematique_fk', Integer(),
                                                   ForeignKey('assuetude_thematique_for_institution.assuetude_thematique_pk'),
                                                   primary_key = True),
                                            useexisting=True,
                                            autoload=autoload)
    return linkInstitutionAssuetudeThematique


def getLinkInstitutionCommuneCouverte(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_commune_couverte'):
        autoload = True
    linkInstitutionCommuneCouverte = Table('link_institution_commune_couverte', metadata,
                                            Column('institution_fk', Integer(),
                                                   ForeignKey('institution.institution_pk')),
                                            Column('commune_fk', Integer(),
                                                   ForeignKey('commune.com_pk')),
                                            useexisting=True,
                                            autoload=autoload)
    return linkInstitutionCommuneCouverte


def getLinkInstitutionSousPlateForme(metadata):
    autoload = False
    if metadata.bind.has_table('link_institution_sousplateforme'):
        autoload = True
    linkInstitutionSousPlateForme = Table('link_institution_sousplateforme', metadata,
                                     Column('institution_fk', Integer(),
                                            ForeignKey('institution.institution_pk'),
                                            primary_key = True),
                                     Column('sousplateforme_fk', Integer(),
                                            ForeignKey('sousplateforme.sousplateforme_pk'),
                                            primary_key = True),
                                     useexisting=True,
                                     autoload=autoload)
    return linkInstitutionSousPlateForme


def getAllSupport(metadata):
    autoload = False
    if metadata.bind.has_table('support'):
        autoload = True
    support = Table('support', metadata,
                    Column('support_pk', Integer(),
                           Sequence('support_support_pk_seq'),
                           primary_key = True),
                    Column('support_titre', Text()),
                    Column('support_description', Text()),
                    Column('support_actif', Boolean()),
                    Column('support_creation_date', DateTime()),
                    Column('support_modification_date', DateTime(), default = func.now()),
                    Column('support_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return support


def getAllRessource(metadata):
    autoload = False
    if metadata.bind.has_table('ressource'):
        autoload = True
    ressource = Table('ressource', metadata,
                    Column('ressource_pk', Integer(),
                           Sequence('ressource_ressource_pk_seq'),
                           primary_key = True),
                    Column('ressource_titre', Text()),
                    Column('ressource_description', Text()),
                    Column('ressource_auteur', Text()),
                    Column('ressource_collection', Text()),
                    Column('ressource_edition', Text()),
                    Column('ressource_date_edition', Text()),
                    Column('ressource_lieu_edition', Text()),
                    Column('ressource_public', Text()),
                    Column('ressource_autre_info', Text()),
                    Column('ressource_lien_pipsa', Text()),
                    Column('ressource_autre_lien', Text()),
                    Column('ressource_objectif', Text()),
                    Column('ressource_utilisation', Text()),
                    Column('ressource_avis_clps', Text()),
                    Column('ressource_disponible_clps', Boolean()),
                    Column('ressource_disponible_autre', Text()),
                    Column('ressource_etat', Text()),
                    Column('ressource_plate_forme_sante_ecole', Boolean()),
                    Column('ressource_plate_forme_assuetude', Boolean()),
                    Column('ressource_plate_forme_sante_famille', Boolean()),
                    Column('ressource_plate_forme_sante_environnement', Boolean()),
                    Column('ressource_mission_centre_documentation', Boolean()),
                    Column('ressource_mission_accompagnement_projet', Boolean()),
                    Column('ressource_mission_reseau_echange', Boolean()),
                    Column('ressource_mission_formation', Boolean()),
                    Column('ressource_creation_date', DateTime()),
                    Column('ressource_modification_date', DateTime(), default = func.now()),
                    Column('ressource_modification_employe', Text()),
                    autoload=autoload,
                    useexisting=True)
    return ressource


def getLinkRessourceMotCle(metadata):
    autoload = False
    if metadata.bind.has_table('link_ressource_mot_cle'):
        autoload = True
    linkRessourceMotCle = Table('link_ressource_mot_cle', metadata,
                                          Column('ressource_fk', Integer(),
                                                 ForeignKey('ressource.ressource_pk'),
                                                 primary_key = True),
                                          Column('motcle_fk', Integer(),
                                                 ForeignKey('mot_cle.motcle_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkRessourceMotCle


def getLinkRessourceTheme(metadata):
    autoload = False
    if metadata.bind.has_table('link_ressource_theme'):
        autoload = True
    linkRessourceTheme = Table('link_ressource_theme', metadata,
                                          Column('ressource_fk', Integer(),
                                                 ForeignKey('ressource.ressource_pk'),
                                                 primary_key = True),
                                          Column('theme_fk', Integer(),
                                                 ForeignKey('theme.theme_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkRessourceTheme


def getLinkRessourcePublic(metadata):
    autoload = False
    if metadata.bind.has_table('link_ressource_public'):
        autoload = True
    linkRessourcePublic = Table('link_ressource_public', metadata,
                                          Column('ressource_fk', Integer(),
                                                 ForeignKey('ressource.ressource_pk'),
                                                 primary_key = True),
                                          Column('public_fk', Integer(),
                                                 ForeignKey('public.public_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkRessourcePublic


def getLinkRessourceSupport(metadata):
    autoload = False
    if metadata.bind.has_table('link_ressource_support'):
        autoload = True
    linkRessourceSupport = Table('link_ressource_support', metadata,
                                  Column('ressource_fk', Integer(),
                                         ForeignKey('ressource.ressource_pk'),
                                         primary_key = True),
                                  Column('support_fk', Integer(),
                                         ForeignKey('support.support_pk'),
                                         primary_key = True),
                                  useexisting=True,
                                  autoload=autoload)
    return linkRessourceSupport


def getLinkRessourceClps(metadata):
    autoload = False
    if metadata.bind.has_table('link_ressource_clps'):
        autoload = True
    linkRessourceClps = Table('link_ressource_clps', metadata,
                                  Column('ressource_fk', Integer(),
                                         ForeignKey('ressource.ressource_pk'),
                                         primary_key = True),
                                  Column('clps_fk', Integer(),
                                         ForeignKey('clps.clps_pk'),
                                         primary_key = True),
                                  useexisting=True,
                                  autoload=autoload)
    return linkRessourceClps


def getAllExperience(metadata):
    autoload = False
    if metadata.bind.has_table('experience'):
        autoload = True
    experience = Table('experience', metadata,
                  Column('experience_pk', Integer(),
                         Sequence('experience_experience_pk_seq'),
                         primary_key = True),
                  Column('experience_titre', Text()),
                  Column('experience_resume', Text()),
                  Column('experience_personne_contact', Text()),
                  Column('experience_personne_contact_email', Text()),
                  Column('experience_personne_contact_telephone', Text()),
                  Column('experience_personne_contact_institution', Text()),
                  Column('experience_element_contexte', Text()),
                  Column('experience_objectif', Text()),
                  Column('experience_public_vise', Text()),
                  Column('experience_demarche_actions', Text()),
                  Column('experience_commune_international', Text()),
                  Column('experience_territoire_tout_brabant_wallon', Boolean()),
                  Column('experience_periode_deroulement', Text()),
                  Column('experience_moyens', Text()),
                  Column('experience_evaluation_enseignement', Text()),
                  Column('experience_perspective_envisagee', Text()),
                  Column('experience_institution_porteur_autre', Text()),
                  Column('experience_institution_partenaire_autre', Text()),
                  Column('experience_institution_ressource_autre', Text()),
                  Column('experience_institution_outil_autre', Text()),
                  Column('experience_formation_suivie', Text()),
                  Column('experience_autres_ressources', Text()),
                  Column('experience_aller_plus_loin', Text()),
                  Column('experience_plate_forme_sante_ecole', Boolean()),
                  Column('experience_plate_forme_assuetude', Boolean()),
                  Column('experience_plate_forme_sante_famille', Boolean()),
                  Column('experience_plate_forme_sante_environnement', Boolean()),
                  Column('experience_mission_centre_documentation', Boolean()),
                  Column('experience_mission_accompagnement_projet', Boolean()),
                  Column('experience_mission_reseau_echange', Boolean()),
                  Column('experience_mission_formation', Boolean()),
                  Column('experience_creation_date', DateTime(), default = func.now()),
                  Column('experience_creation_employe', Text()),
                  Column('experience_modification_date', DateTime(), default = func.now()),
                  Column('experience_modification_employe', Text()),
                  Column('experience_etat', Text()),
                  Column('experience_publication_siss', Boolean()),
                  Column('experience_auteur_login', Text()),
                  Column('experience_auteur_fk', Integer(),
                           ForeignKey('auteur.auteur_pk'),
                           nullable=False),
                  autoload=autoload,
                  useexisting=True)
    return experience


def getLinkExperienceInstitutionPorteur(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_institution_porteur'):
        autoload = True
    linkExperienceInstitutionPorteur = Table('link_experience_institution_porteur', metadata,
                                                 Column('experience_fk', Integer(),
                                                        ForeignKey('experience.experience_pk'),
                                                        primary_key=True),
                                                 Column('institution_fk', Integer(),
                                                        ForeignKey('institution.institution_pk'),
                                                        primary_key=True),
                                                 useexisting=True,
                                                 autoload=autoload)
    return linkExperienceInstitutionPorteur


def getLinkExperienceInstitutionPartenaire(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_institution_partenaire'):
        autoload = True
    linkExperienceInstitutionPartenaire = Table('link_experience_institution_partenaire', metadata,
                                                  Column('experience_fk', Integer(),
                                                         ForeignKey('experience.experience_pk'),
                                                         primary_key=True),
                                                  Column('institution_fk', Integer(),
                                                          ForeignKey('institution.institution_pk'),
                                                          primary_key=True),
                                                  useexisting=True,
                                                  autoload=autoload)
    return linkExperienceInstitutionPartenaire


def getLinkExperienceInstitutionRessource(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_institution_ressource'):
        autoload = True
    linkExperienceInstitutionRessource = Table('link_experience_institution_ressource', metadata,
                                                Column('experience_fk', Integer(),
                                                       ForeignKey('experience.experience_pk'),
                                                       primary_key=True),
                                                Column('institution_fk', Integer(),
                                                       ForeignKey('institution.institution_pk'),
                                                       primary_key=True),
                                                useexisting=True,
                                                autoload=autoload)
    return linkExperienceInstitutionRessource


def getLinkExperienceRessource(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_ressource'):
        autoload = True
    linkExperienceRessource = Table('link_experience_ressource', metadata,
                                     Column('experience_fk', Integer(),
                                            ForeignKey('experience.experience_pk'),
                                            primary_key = True),
                                     Column('ressource_fk', Integer(),
                                            ForeignKey('ressource.ressource_pk'),
                                            primary_key = True),
                                     useexisting=True,
                                     autoload=autoload)
    return linkExperienceRessource


def getLinkExperienceMilieuDeVie(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_milieudevie'):
        autoload = True
    linkExperienceMilieuDeVie = Table('link_experience_milieudevie', metadata,
                                     Column('experience_fk', Integer(),
                                            ForeignKey('experience.experience_pk'),
                                            primary_key = True),
                                     Column('milieudevie_fk', Integer(),
                                            ForeignKey('milieudevie.milieudevie_pk'),
                                            primary_key = True),
                                     useexisting=True,
                                     autoload=autoload)
    return linkExperienceMilieuDeVie


def getLinkExperienceSousPlateForme(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_sousplateforme'):
        autoload = True
    linkExperienceSousPlateForme = Table('link_experience_sousplateforme', metadata,
                                     Column('experience_fk', Integer(),
                                            ForeignKey('experience.experience_pk'),
                                            primary_key = True),
                                     Column('sousplateforme_fk', Integer(),
                                            ForeignKey('sousplateforme.sousplateforme_pk'),
                                            primary_key = True),
                                     useexisting=True,
                                     autoload=autoload)
    return linkExperienceSousPlateForme


def getLinkExperienceMotCle(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_mot_cle'):
        autoload = True
    linkExperienceMotCle = Table('link_experience_mot_cle', metadata,
                                          Column('experience_fk', Integer(),
                                                 ForeignKey('experience.experience_pk'),
                                                 primary_key = True),
                                          Column('motcle_fk', Integer(),
                                                 ForeignKey('mot_cle.motcle_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkExperienceMotCle


def getLinkExperienceCommune(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_commune'):
        autoload = True
    linkExperienceCommune = Table('link_experience_commune', metadata,
                                          Column('experience_fk', Integer(),
                                                 ForeignKey('experience.experience_pk'),
                                                 primary_key = True),
                                          Column('commune_fk', Integer(),
                                                 ForeignKey('commune.com_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkExperienceCommune


def getLinkExperienceTheme(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_theme'):
        autoload = True
    linkExperienceTheme = Table('link_experience_theme', metadata,
                                          Column('experience_fk', Integer(),
                                                 ForeignKey('experience.experience_pk'),
                                                 primary_key = True),
                                          Column('theme_fk', Integer(),
                                                 ForeignKey('theme.theme_pk'),
                                                 primary_key = True),
                                          useexisting=True,
                                          autoload=autoload)
    return linkExperienceTheme


def getLinkExperiencePublic(metadata):
    autoload = False
    if metadata.bind.has_table('link_experience_public'):
        autoload = True
    linkExperiencePublic = Table('link_experience_public', metadata,
                                  Column('experience_fk', Integer(),
                                         ForeignKey('experience.experience_pk'),
                                         primary_key = True),
                                  Column('public_fk', Integer(),
                                         ForeignKey('public.public_pk'),
                                         primary_key = True),
                                  useexisting=True,
                                  autoload=autoload)
    return linkExperiencePublic


def getAllRecit(metadata):
    autoload = False
    if metadata.bind.has_table('recit'):
        autoload = True
    recit = Table('recit', metadata,
                  Column('recit_pk', Integer(),
                         Sequence('recit_recit_pk_seq'),
                         primary_key = True),
                  Column('recit_description', Text()),
                  autoload=autoload,
                  useexisting=True)
    return recit


def getAllAuteur(metadata):
    autoload = False
    if metadata.bind.has_table('auteur'):
        autoload = True
    auteur = Table('auteur', metadata,
                   Column('auteur_pk', Integer(),
                           Sequence('auteur_auteur_pk_seq', optional=True),
                           primary_key = True),
                   Column('auteur_nom', Text()),
                   Column('auteur_prenom', Text()),
                   Column('auteur_email', Text()),
                   Column('auteur_login', Text()),
                   Column('auteur_pass', Text()),
                   Column('auteur_institution', Text()),
                   Column('auteur_id_filemaker', Text()),
                   Column('auteur_creation_date', DateTime()),
                   Column('auteur_actif', Boolean(), default = True),
                   Column('auteur_for_experience', Boolean(), default = False),
                   Column('auteur_for_institution', Boolean(), default = False),
                   Column('auteur_clps_fk', Integer(),
                           ForeignKey('clps.clps_pk'),
                           nullable=False),
                   Column('auteur_modification_date', DateTime(), default = func.now()),
                   Column('auteur_modification_employe', Text()),
                   autoload=autoload)
    return auteur


def getAllRechercheLog(metadata):
    autoload = False
    if metadata.bind.has_table('recherche_log'):
        autoload = True
    rechercheLog = Table('recherche_log', metadata,
                             Column('recherchelog_pk', Integer(),
                                    Sequence('recherche_log_recherchelog_pk_seq', optional=True),
                                    primary_key = True),
                             Column('recherchelog_requete', Text()),
                             Column('recherchelog_user', Text()),
                             Column('recherchelog_experience_fk', Integer()),
                             Column('recherchelog_milieudevie_fk', Integer()),
                             Column('recherchelog_theme_fk', Integer()),
                             Column('recherchelog_public_fk', Integer()),
                             Column('recherchelog_motcle_fk', Integer()),
                             Column('recherchelog_date', DateTime(), default = func.now()),
                    autoload=autoload)
    return rechercheLog
