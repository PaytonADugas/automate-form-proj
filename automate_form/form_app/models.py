from django.db import models

from random import randrange

# Choices
TRUE_FALSE_CHOICES = (
    ('empty', 'select'),
    ('Yes', 'Yes'),
    ('No', 'No')
)
GENDER_CHOICES = (
    ('empty', 'select'),
    ('Male', 'Male'),
    ('Female', 'Famale')
)
GRADE_CHOICES = (
    ('empty', 'select'),
    ('k5', 'k5'),
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
)
SCHOOL_YEAR_CHOICES = (
    ('empty', 'select'),
    ('2021/2022', '2021/2022')
)

# test model

class Test_model(models.Model):
    student_id = 'default'

    name = models.CharField(max_length=256)
    age = models.IntegerField(max_length=256)
    is_employed = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    date = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# Model of a NCCS student

class NCCS_Student(models.Model):

    student_id = 'default'

    # STUDENT INFORMATION

    last_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    birth_date = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES, default=None)
    disabilities = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)

    # ACADEMIC INFORMATION

    school_year = models.CharField(max_length=256, choices=SCHOOL_YEAR_CHOICES, default=None)
    grade = models.CharField(max_length=256, choices=GRADE_CHOICES, default=None)

    # ACADEMIC RECORDS

    # We give permission to have our student's record requested from their previous school?
    record_permission = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # private, public, homeschooled
    previous_school_year = models.CharField(max_length=256)
    previous_school = models.CharField(max_length=256)
    previous_school_mailing_address = models.CharField(max_length=256)
    # Previous school information
    previous_school_city = models.CharField(max_length=256)
    previous_school_state = models.CharField(max_length=256)
    previous_school_zip = models.CharField(max_length=256)
    previous_school_phone = models.CharField(max_length=256)
    previous_school_been_suspended = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)

    # FAMILY INFORMATION

    father_name = models.CharField(max_length=256)
    father_employment = models.CharField(max_length=256)
    mother_name = models.CharField(max_length=256)
    mother_employment = models.CharField(max_length=256)
    family_address = models.CharField(max_length=256)
    family_city = models.CharField(max_length=256)
    family_state = models.CharField(max_length=256)
    family_zip = models.CharField(max_length=256)
    family_phone = models.CharField(max_length=256)
    family_email = models.CharField(max_length=256)
    # With whom is the student currently living?
    student_living_with = models.CharField(max_length=256)
    student_guardian = models.CharField(max_length=256)
    family_church = models.CharField(max_length=256)

    # HSLDA INFORMATION

    # Do you hold Home School Legal Defense Association membership?
    HSLDA_membership = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)

    # FACULTY INFORMATION

    #Who will be the primary teacher, at home with the student, during school hours?
    primary_teacher = models.CharField(max_length=256)
    high_school_eduication = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    college_eduication = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    list_training = models.CharField(max_length=256)

    # PARENTAL RESPONSIBILITY AGREEMENT

    # We will apply to HSLDA for membership OR we will renew our HSLDA membership each year that we are enrolled in NCCS.
    membership_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We will provide curriculum for student in compliance with state guidelines for subjects to be taught.
    curriculum_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We understand the importance of accurate record keeping and agree to maintain a daily lesson plan book that records what was accomplished in each subject and we will keep these records for, at least, a two year period.
    record_keeping_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We understand it is the parent’s responsibility to provide curriculum, do lesson planning, maintain a record of daily work, evaluate our student’s progress and that all decisions relating to educational philosophy and methods, style, selection of books, teaching material and curriculum, grading and evaluations are our responsibility. Therefore, the outcome of your student’s education rests on your efforts and that of your students.
    parent_participation_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # One parent will be at home during school hours and teaching our student in an orderly and systematic manner, at least 180 days of the year.
    parent_home_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We will enter attendance and grades at the times specified on the school calendar, realizing that timely attendance reporting is absolutely essential in an independent study program.
    attendance_grades_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We will post our elementary student’s proposed course of study and/or high school student’s course description on their report card page at the beginning of the school year.
    course_of_study_course_description_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We understand that the School Calendar, NCCS Handbook, and the NCCS High School Manual have important dates and information that we need to know in order to work responsibly with NCCS. We agree to read through the Handbook/Manual and review the school calendar and acquainted ourselves with the school services and our responsibilities.
    read_handbook_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We will notify NCCS if and when we enroll our student in another school as a matter of courtesy.
    change_schools_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # We realize that our student will be dismissed from enrollment if: 1) We fail to do our record keeping in accordance with the NCCS Handbook. 2) We fail to comply with Parental Responsibility Agreement in any way.
    enrolment_dismissal_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    # Although we believe it is the parent’s responsibility to direct their student’s education we have policies that may conflict with some family’s strategy. We feel these policies help support the integrity of North County Christian School. We will attempt to accommodate each parent’s philosophy and goals as much as possible.
    parent_direction_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)

    # SIGNATURE

    read_agreement = models.CharField(max_length=256, choices=TRUE_FALSE_CHOICES, default=None)
    father_signature = models.CharField(max_length=256)
    father_sign_date = models.CharField(max_length=256)
    mother_signature = models.CharField(max_length=256)
    mother_sign_date = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name
