from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


degreeprograms_vocab = ([
        SimpleTerm(value=u'AppliedMath', title=_(u'Applied Mathematics (Arts & Sciences)')),
        SimpleTerm(value=u'Biochemistry', title=_(u'Biochemistry (Arts & Sciences)')),
        SimpleTerm(value=u'ChemBioEngineering', title=_(u'Chemical and Biological Engineering (listed as Chemical Engineering in College of Engineering & Applied Science)')),
        SimpleTerm(value=u'ComputerScience', title=_(u'Computer Science (Engineering & Applied Science)')),
        SimpleTerm(value=u'Ecology', title=_(u'Ecology and Evolutionary Biology (Arts & Sciences)')),
        SimpleTerm(value=u'Mechanical', title=_(u'Mechanical Engineering (Engineering & Applies Science)')),
        SimpleTerm(value=u'Molecular', title=_(u'Molecular, Cellular and Developmental Biology (Arts & Sciences)')),
        SimpleTerm(value=u'ChemicalPhysics', title=_(u'Chemical Physics (Arts & Sciences).')),
        ])

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


def comp_sci_financial_aid_vocab(context):
    return ([
    SimpleTerm(value=u'MustHave', title=_(u'I will not accept admission without financial aid.')),
    SimpleTerm(value=u'WillConsider', title=_(u'I have my own financial support, but would like to be considered for financial aid.')),
    SimpleTerm(value=u'DoNotWant', title=_(u'I do not wish to be considered for financial aid.')),
    ])


def yes_no_vocab (context):
    return ([
    SimpleTerm(value=u'', title=_(u'-----')),
    SimpleTerm(value=u'Yes', title=_(u'Yes')),
    SimpleTerm(value=u'No', title=_(u'No')),
    ])


def exp_or_theoretical_vocab (context):
    return ([
    SimpleTerm(value=u'Experimental', title=_(u'Experimental')),
    SimpleTerm(value=u'Theoretical', title=_(u'Theoretical')),
    ])
