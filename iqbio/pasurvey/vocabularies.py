from zope.schema.vocabulary import SimpleVocabulary

#----------------------------------------------------------------------
def biochem_research_interests_vocab(context):
    ''' '''
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
    ''' '''
    vocab = ('Thomas R. Cech',
        'Kristi S. Anseth',
        'Meredith D. Betterton',
        'David M. Bortz',
        'Stephanie J. Bryant',
        'Aaron Clauset',
        'Robin Dowell',
        'Virginia L. Ferguson',
        'Matthew A. Glaser',
        'Debra S. Goldberg',
        'Rob Knight',
        'Leslie A. Leinwand',
        'Manuel E. Lladser',
        'Brett A. Melbourne',
        'David. J. Nesbitt',
        'Arthur Pardi',
        'Amy. E. Palmer',
        'Thomas T. Perkins',
        'Hang (Hubert) Yin',
        )
    return SimpleVocabulary.fromValues(vocab)



def degreeprograms_vocab(context):
    ''' '''
    vocab = (
        'Applied Mathematics (Arts & Sciences)',
        'Biochemistry (Arts & Sciences)',
        'Chemical and Biological Engineering (listed as Chemical Engineering in College of Engineering & Applied Science)',
        'Computer Science (Engineering & Applied Science)',
        'Ecology and Evolutionary Biology (Arts & Sciences)',
        'Mechanical Engineering (Engineering & Applies Science)',
        'Molecular, Cellular and Developmental Biology (Arts & Sciences)',
        'Chemical Physics (Arts & Sciences).',
        )
    return SimpleVocabulary.fromValues(vocab)


def biochem_vocab(context):
    vocab = (
        'Bio-Organic and Bio-Inorganic',
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


def chem_bio_vocab(context):
    vocab = ('Advanced Ceramic Materials',
        'Applied Math and Computers',
        'Biomedical Engineering',
        'Biotechnology',
        'Catalysis/Surface Phenomena',
        'Energy/Environmental Engineering',
        'Fluid Dynamics',
        'Materials/Nanomaterials',
        'Membrane Science',
        'Multiphase Flow Systems',
        'Particle Technology',
        'Polymer Science',
        'Powder Processing',
        'Process Control/Optimization',
        'Reaction Engineering',
        'Separations',
        'Thermodynamics',
        'Transport Processes',
    )
    return SimpleVocabulary.fromValues(vocab)


def comp_sci_vocab(context):
    vocab = (
        'Bio and Medical Informatics',
        'Computational Modeling of Human Cognition',
        'Computational Science',
        'Computer Architecture',
        'Database Systems',
        'Distributed and Network Computing',
        'Human-Centered Computing',
        'Machine Learning',
        'Machine Vision',
        'Numerical and Scientific Computation',
        'Operating Systems',
        'Programming Languages',
        'Robotics',
        'Security',
        'Software Engineering',
        'Speech and Language Processing',
        'Theory',
    )
    return SimpleVocabulary.fromValues(vocab)
