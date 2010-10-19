from zope.schema.vocabulary import SimpleVocabulary

def sandia_org_vocabulary(context):
    sandia_org_vocab= ('09326', '09328', 'unknown/tbd', )
    return SimpleVocabulary.fromValues(sandia_org_vocab)


#----------------------------------------------------------------------
def  biochem_research_interests_vocab(context):
    """ """
    vocab = ('Bio-Organic and Bio-Inorganic',
        'Informatics and Proteomics',
        'Nucleic Acids',
        'Cell Signaling',
        'Membranes',
        'Proteins and Enzymology',
        'Chemical Biology/Genetics',
        'Molecular Biophysics',
        'Structural Biology',
        'Chemical Physics',
        'Biophysics',
        'Atmospheric/Astrochemistry',
        'Kinetics/Thermodynamics',
        'Reaction Dynamics',
        'Surface Chemistry',
        'Photochemistry',
        'Physical Organic Chemistry',
        'Theoretical Chemistry',
        'Nanotechnology/Materials',
        'Physical Inorganic Chemistry',
        )

    return SimpleVocabulary.fromValues(vocab)




