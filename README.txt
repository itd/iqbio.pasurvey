====================================================
I.Q. Biology Pre-Admission Survey Tool
====================================================

This describes the use and management of the IQ Biology
pre-admissions survey tool.

This program assumes (and will create) a '/surveys/' folder
exists off the site root, and that all submissions will be
handled in the context of that folder.

The Actors:
 * Submitter
 * Survey Manager(s)
 * Faculty Reviewers
 * Graduate Program Reviewers (one group for each program)
 * Manager (standard Plone Manager role)

There are application management Groups configured for
Survey Managers, Faculty Reviewers, and for the various
Graduate Program Reviewers.

Persons who will be fulfilling those roles will need to go to
the site and register for / create an account.

A site Manager will need to identify the person's who
belong to each group and add those users to their respective
groups via Plone's administrative control panel and the Users
and Groups screen (@@usergroup-userprefs).


Survey submission
==================
The process for using the tool is as follows:


Initial Submission - Save as Draft
------------------------------------------

 * A Submitter fills-in the initial form, fills-in the required
   fields, and has the option to save as draft.
   The system sends the user an email with instructions and
   a link back to the site.
   After clicking on the save as draft button, the Submitter
   is prompted to go to the Graduate Admissions site to apply
   to their first degree program of interest.


Final Submission - Submit for Review
------------------------------------------

 * Submitter returns to the surveys folder to complete the Survey,
   filling-in any supplementary information for the degree programs
   they have selected.

 * When the Submitter has completed the survey's supplimentary
   information, Submitter must press the "Submit Survey" button,
   transitioning the survey to the "Pending Faculty Review" state.


Survey Management
===========================


Survey Status Overview
----------------------------------
A list of submissions including their degree program selections,
'accepted' status for each selection, and current workflow state
has been created. Managers and reviewers can use this list to
identify submissions they may need to address. Any manager or
reviewer may view any submission. However, only the specified
reviewers from the specified degree programs may comment and
accept or not accept the submission to their specific program.

The URL for this view is:
http://SITE_URL/surveys/submission-status


Initial Review
-------------------
When a survey is transitioned into the Pending Faculty Review state
the Survey Manager will review the submission for completeness
and has two options:
 1. "Reject" the submission, removing it from the rest of the
    workflow and putting the submission into the "Rejected"
    state, or
 2. Transition the Survey to the Faculty Review state but selecting
    the "Transition to Faculty Review" state transition option.



Faculty Review
-------------------
Assuming a submission has been approved and transitioned to the
Faculty Review state by a Survey Manager, a Faculty Reviewer will
review a submission and either transition it to the not accept it.


Review by Specified Graduate Program Reviewers
----------------------------------------------------


Final Transitions and States
------------------------------


