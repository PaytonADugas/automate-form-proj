from django import forms
from form_app.models import NCCS_Student, Test_model
from attr import attrs



class Student_data(forms.ModelForm):
    class Meta:
        model = NCCS_Student
        fields = '__all__'

        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'disabilities': forms.Select(attrs={'class': 'form-control'}),
            'school_year': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'record_permission': forms.Select(attrs={'class': 'form-control'}),
            'previous_school_year': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_mailing_address': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_city': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_state': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_school_been_suspended': forms.Select(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_employment': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_employment': forms.TextInput(attrs={'class': 'form-control'}),
            'family_address': forms.TextInput(attrs={'class': 'form-control'}),
            'family_city': forms.TextInput(attrs={'class': 'form-control'}),
            'family_state': forms.TextInput(attrs={'class': 'form-control'}),
            'family_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'family_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'family_email': forms.TextInput(attrs={'class': 'form-control'}),
            'student_living_with': forms.TextInput(attrs={'class': 'form-control'}),
            'student_guardian': forms.TextInput(attrs={'class': 'form-control'}),
            'family_church': forms.TextInput(attrs={'class': 'form-control'}),
            'HSLDA_membership': forms.Select(attrs={'class': 'form-control'}),
            'primary_teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'high_school_eduication': forms.Select(attrs={'class': 'form-control'}),
            'college_eduication': forms.Select(attrs={'class': 'form-control'}),
            'list_training': forms.Textarea(attrs={'class': 'form-control'}),
            'membership_agreement': forms.Select(attrs={'class': 'form-control'}),
            'curriculum_agreement': forms.Select(attrs={'class': 'form-control'}),
            'record_keeping_agreement': forms.Select(attrs={'class': 'form-control'}),
            'parent_participation_agreement': forms.Select(attrs={'class': 'form-control'}),
            'parent_home_agreement': forms.Select(attrs={'class': 'form-control'}),
            'attendance_grades_agreement': forms.Select(attrs={'class': 'form-control'}),
            'course_of_study_course_description_agreement': forms.Select(attrs={'class': 'form-control'}),
            'read_handbook_agreement': forms.Select(attrs={'class': 'form-control'}),
            'change_schools_agreement': forms.Select(attrs={'class': 'form-control'}),
            'enrolment_dismissal_agreement': forms.Select(attrs={'class': 'form-control'}),
            'parent_direction_agreement': forms.Select(attrs={'class': 'form-control'}),
            'read_agreement': forms.Select(attrs={'class': 'form-control'}),
            'father_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'father_sign_date': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_sign_date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Test_data(forms.ModelForm):
    # class Meta:
    #     model = Test_model
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Test_model
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'is_employed': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }
