from zope.schema.vocabulary import SimpleVocabulary

#----------------------------------------------------------------------
def biochem_research_interests_vocab(context):
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


#
def facultyofinterest_vocab(context):
    """ """
    vocab = ('person1',
        'person2',
        'person3',
        )
    return SimpleVocabulary.fromValues(vocab)



def degreeprograms_vocab(context):
    """ """
    vocab = ('program1',
        'program2',
        'program3',
        )
    return SimpleVocabulary.fromValues(vocab)







