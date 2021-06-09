# Generated by Django 3.2.3 on 2021-05-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0002_test_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nccs_student',
            old_name='mailing_address',
            new_name='previous_school_mailing_address',
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='HSLDA_membership',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='attendance_grades_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='birth_date',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='change_schools_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='college_eduication',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='course_of_study_course_description_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='curriculum_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='disabilities',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='enrolment_dismissal_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='father_sign_date',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='gender',
            field=models.CharField(choices=[('empty', 'select'), ('m', 'Male'), ('f', 'Famale')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='grade',
            field=models.CharField(choices=[('empty', 'select'), ('k5', 'k5'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='high_school_eduication',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='membership_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='mother_sign_date',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='parent_direction_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='parent_home_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='parent_participation_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='previous_school_been_suspended',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='read_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='read_handbook_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='record_keeping_agreement',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='record_permission',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='nccs_student',
            name='school_year',
            field=models.CharField(choices=[('empty', 'select'), ('2021/2022', '2021/2022')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='test_model',
            name='age',
            field=models.IntegerField(max_length=256),
        ),
        migrations.AlterField(
            model_name='test_model',
            name='date',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='test_model',
            name='is_employed',
            field=models.CharField(choices=[('empty', 'select'), ('y', 'Yes'), ('n', 'No')], default=None, max_length=256),
        ),
    ]