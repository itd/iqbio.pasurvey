from zope.schema.vocabulary import SimpleVocabulary
from iqbio.pasurvey import _

degreeprograms_vocab = SimpleVocabulary.fromItems((
    ('Applied Mathematics (Arts & Sciences)', 'AppliedMath'),
    ('Biochemistry (Arts & Sciences)', 'Biochemistry'),
    ('Chemical and Biological Engineering (listed as Chemical Engineering in College of Engineering & Applied Science)', 'ChemBioEngineering'),
    ('Computer Science (Engineering & Applied Science)', 'ComputerScience'),
    ('Ecology and Evolutionary Biology (Arts & Sciences)', 'Ecology'),
    ('Mechanical Engineering (Engineering & Applies Science)', 'Mechanical'),
    ('Molecular, Cellular and Developmental Biology (Arts & Sciences)', 'Molecular'),
    ('Chemical Physics (Arts & Sciences).', 'ChemicalPhysics'),
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
    ('Thomas R. Cech', 'Cech'),
    ('Kristi S. Anseth','Anseth'),
    ('Meredith D. Betterton','Betterton'),
    ('David M. Bortz','Bortz'),
    ('Stephanie J. Bryant','Bryant'),
    ('Aaron Clauset','Clauset'),
    ('Robin Dowell','Dowell'),
    ('Virginia L. Ferguson','Ferguson'),
    ('Matthew A. Glaser','Glaser'),
    ('Debra S. Goldberg','Goldberg'),
    ('Rob Knight','Knight'),
    ('Leslie A. Leinwand','Leinwand'),
    ('Manuel E. Lladser','Lladser'),
    ('Brett A. Melbourne','Melbourne'),
    ('David. J. Nesbitt','Nesbitt'),
    ('Arthur Pardi','Pardi'),
    ('Amy. E. Palmer','Palmer'),
    ('Thomas T. Perkins','Perkins'),
    ('Hang (Hubert) Yin', 'Yin'),
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
    (u'I will not accept admission without financial aid.', 'MustHave'),
    ( u'I have my own financial support, but would like to be considered for financial aid.', 'WillConsider'),
    (u'I do not wish to be considered for financial aid.', 'DoNotWant'),
    ))

yes_no_vocab = SimpleVocabulary.fromItems((
    (u'', ''),
    (u'Yes', 'Yes'),
    (u'No', 'No'),
    ))


exp_or_theoretical_vocab = SimpleVocabulary.fromItems((
    ('Experimental', u'Experimental'),
    ('Theoretical', u'Theoretical'),
    ))
