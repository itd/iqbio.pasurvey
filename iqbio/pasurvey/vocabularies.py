from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from iqbio.pasurvey import _

degreeprograms_vocab = SimpleVocabulary(
    [SimpleTerm(title='Applied Mathematics (Arts & Sciences)',
                value='AppliedMath'),
     SimpleTerm(title='Biochemistry (Arts & Sciences)',
                value='Biochemistry'),
     SimpleTerm(title='Chemical and Biological Engineering (listed as Chemical Engineering in College of Engineering & Applied Science)',
                value='ChemBioEngineering'),
     SimpleTerm(title='Computer Science (Engineering & Applied Science)',
                value='ComputerScience'),
     SimpleTerm(title='Ecology and Evolutionary Biology (Arts & Sciences)',
                value='Ecology'),
     SimpleTerm(title='Mechanical Engineering (Engineering & Applies Science)',
                value='Mechanical'),
     SimpleTerm(title='Molecular, Cellular and Developmental Biology (Arts & Sciences)',
                value='Molecular'),
     SimpleTerm(title='Chemical Physics (Arts & Sciences).',
                value='ChemicalPhysics')]
    )

degreeprograms_lite_vocab = SimpleVocabulary(
    [SimpleTerm(title='Applied Mathematics',
                value='AppliedMath'),
     SimpleTerm(title='Biochemistry',
                value='Biochemistry'),
     SimpleTerm(title='Chemical and Biological Engineering',
                value='ChemBioEngineering'),
     SimpleTerm(title='Computer Science',
                value='ComputerScience'),
     SimpleTerm(title='Ecology and Evolutionary Biology',
                value='Ecology'),
     SimpleTerm(title='Mechanical Engineering',
                value='Mechanical'),
     SimpleTerm(title='Molecular, Cellular and Developmental Biology',
                value='Molecular'),
     SimpleTerm(title='Chemical Physics',
                value='ChemicalPhysics')]
    )
#----------------------------------------------------------------------
biochem_research_interests_vocab = SimpleVocabulary.fromValues((
    ('Bio-Organic and Bio-Inorganic'),
    ('Informatics and Proteomics'),
    ('Nucleic Acids'),
    ('Cell Signaling'),
    ('Membranes'),
    ('Proteins and Enzymology'),
    ('Chemical Biology/Genetics'),
    ('Molecular Biophysics'),
    ('Structural Biology'),
    ('Chemical Physics'),
    ('Biophysics'),
    ('Atmospheric/Astrochemistry'),
    ('Kinetics/Thermodynamics'),
    ('Reaction Dynamics'),
    ('Surface Chemistry'),
    ('Photochemistry'),
    ('Physical Organic Chemistry'),
    ('Theoretical Chemistry'),
    ('Nanotechnology/Materials'),
    ('Physical Inorganic Chemistry'),
    ))


facultyofinterest_vocab = SimpleVocabulary((
    SimpleTerm(title='Thomas R. Cech', value='Cech'),
    SimpleTerm(title='Kristi S. Anseth',value='Anseth'),
    SimpleTerm(title='Meredith D. Betterton',value='Betterton'),
    SimpleTerm(title='David M. Bortz',value='Bortz'),
    SimpleTerm(title='Stephanie J. Bryant',value='Bryant'),
    SimpleTerm(title='Aaron Clauset',value='Clauset'),
    SimpleTerm(title='Robin Dowell',value='Dowell'),
    SimpleTerm(title='Virginia L. Ferguson',value='Ferguson'),
    SimpleTerm(title='Matthew A. Glaser',value='Glaser'),
    SimpleTerm(title='Debra S. Goldberg',value='Goldberg'),
    SimpleTerm(title='Rob Knight',value='Knight'),
    SimpleTerm(title='Leslie A. Leinwand',value='Leinwand'),
    SimpleTerm(title='Manuel E. Lladser',value='Lladser'),
    SimpleTerm(title='Brett A. Melbourne',value='Melbourne'),
    SimpleTerm(title='David. J. Nesbitt',value='Nesbitt'),
    SimpleTerm(title='Arthur Pardi',value='Pardi'),
    SimpleTerm(title='Amy E. Palmer',value='Palmer'),
    SimpleTerm(title='Thomas T. Perkins',value='Perkins'),
    SimpleTerm(title='Hang (Hubert) Yin', value='Yin'),
    ))



bio_chem_vocab = SimpleVocabulary.fromValues((
    ('Bio-Organic and Bio-Inorganic'),
    ('Informatics and Proteomics'),
    ('Nucleic Acids'),
    ('Cell Signaling'),
    ('Membranes'),
    ('Proteins and Enzymology'),
    ('Chemical Biology/Genetics'),
    ('Molecular Biophysics'),
    ('Structural Biology'),
    ('Chemical Physics'),
    ('Biophysics'),
    ('Atmospheric/Astrochemistry'),
    ('Kinetics/Thermodynamics'),
    ('Reaction Dynamics'),
    ('Surface Chemistry'),
    ('Photochemistry'),
    ('Physical Organic Chemistry'),
    ('Theoretical Chemistry'),
    ('Nanotechnology/Materials'),
    ('Physical Inorganic Chemistry'),
    ))


chem_bio_vocab = SimpleVocabulary.fromValues((
        'Advanced Ceramic Materials',
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
    ))


comp_sci_vocab = SimpleVocabulary.fromValues((
    ('Bio and Medical Informatics'),
    ('Computational Modeling of Human Cognition'),
    ('Computational Science'),
    ('Computer Architecture'),
    ('Database Systems'),
    ('Distributed and Network Computing'),
    ('Human-Centered Computing'),
    ('Machine Learning'),
    ('Machine Vision'),
    ('Numerical and Scientific Computation'),
    ('Operating Systems'),
    ('Programming Languages'),
    ('Robotics'),
    ('Security'),
    ('Software Engineering'),
    ('Speech and Language Processing'),
    ('Theory'),
    ))

comp_sci_financial_aid_vocab = SimpleVocabulary((
    SimpleTerm(title=u'I will not accept admission without financial aid.', value='MustHave'),
    SimpleTerm(title=u'I have my own financial support, but would like to be considered for financial aid.', value='WillConsider'),
    SimpleTerm(title=u'I do not wish to be considered for financial aid.', value='DoNotWant'),
    ))

yes_no_vocab = SimpleVocabulary((
    SimpleTerm(title=u'', value=''),
    SimpleTerm(title=u'Yes', value='Yes'),
    SimpleTerm(title=u'No', value='No'),
    ))


exp_or_theoretical_vocab = SimpleVocabulary((
    SimpleTerm(value='Experimental', title=u'Experimental'),
    SimpleTerm(value='Theoretical', title=u'Theoretical'),
    ))
