from zope.schema.vocabulary import SimpleVocabulary
from iqbio.pasurvey import _

degreeprograms_vocab = SimpleVocabulary.fromItems((
    ('AppliedMath', 'Applied Mathematics (Arts & Sciences)'),
    ('Biochemistry', 'Biochemistry (Arts & Sciences)'),
    ('ChemBioEngineering', 'Chemical and Biological Engineering (listed as Chemical Engineering in College of Engineering & Applied Science)'),
    ('ComputerScience', 'Computer Science (Engineering & Applied Science)'),
    ('Ecology', 'Ecology and Evolutionary Biology (Arts & Sciences)'),
    ('Mechanical', 'Mechanical Engineering (Engineering & Applies Science)'),
    ('Molecular', 'Molecular, Cellular and Developmental Biology (Arts & Sciences)'),
    ('ChemicalPhysics', 'Chemical Physics (Arts & Sciences).'),
    ))

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


facultyofinterest_vocab = SimpleVocabulary.fromItems((
    ('Cech', 'Thomas R. Cech'),
    ('Anseth', 'Kristi S. Anseth'),
    ('Betterton', 'Meredith D. Betterton'),
    ('Bortz', 'David M. Bortz'),
    ('Bryant', 'Stephanie J. Bryant'),
    ('Clauset', 'Aaron Clauset'),
    ('Dowell', 'Robin Dowell'),
    ('Ferguson', 'Virginia L. Ferguson'),
    ('Glaser', 'Matthew A. Glaser'),
    ('Goldberg', 'Debra S. Goldberg'),
    ('Knight', 'Rob Knight'),
    ('Leinwand', 'Leslie A. Leinwand'),
    ('Lladser', 'Manuel E. Lladser'),
    ('Melbourne', 'Brett A. Melbourne'),
    ('Nesbitt', 'David. J. Nesbitt'),
    ('Pardi', 'Arthur Pardi'),
    ('Palmer', 'Amy. E. Palmer'),
    ('Perkins', 'Thomas T. Perkins'),
    ('Yin', 'Hang (Hubert) Yin'),
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

comp_sci_financial_aid_vocab = SimpleVocabulary.fromItems((
    ('MustHave', u'I will not accept admission without financial aid.'),
    ('WillConsider', u'I have my own financial support, but would like to be considered for financial aid.'),
    ('DoNotWant', u'I do not wish to be considered for financial aid.'),
    ))

yes_no_vocab = SimpleVocabulary.fromItems((
    ('', u'-----'),
    ('Yes', u'Yes'),
    ('No', u'No'),
    ))


exp_or_theoretical_vocab = SimpleVocabulary.fromItems((
    ('Experimental', u'Experimental'),
    ('Theoretical', u'Theoretical'),
    ))
