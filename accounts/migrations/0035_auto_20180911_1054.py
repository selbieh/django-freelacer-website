# Generated by Django 2.0.4 on 2018-09-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20180911_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='specialty',
            field=models.CharField(choices=[('Websites, IT, & Software', [('Build An Online Store', 'Build An Online Store'), ('Convert A Template To A Website', 'Convert A Template To A Website'), ('Create A Wordpress Template', 'Create A Wordpress Template'), ('Create A Drupal Template', 'Create A Drupal Template'), ('dashboard', 'dashboard'), ('API Opencart', 'API Opencart'), ('Website Redesigning Contest', 'Website Redesigning Contest'), ('I want someone to do SEO for my site', 'I want someone to do SEO for my site'), ('An Ecosystem for Bilibit and mainpage website using wordpress or scratch', 'An Ecosystem for Bilibit and mainpage website using wordpress or scratch'), ('Web applications', 'Web applications'), ('Website design', 'Website design'), ('logo design', 'logo design'), ('Build an online wordpress ecommerce publication', 'Build an online wordpress ecommerce publication'), ('I am looking for someone to build a website for the launch of a book', 'I am looking for someone to build a website for the launch of a book')]), ('Mobile Development', [('Develop An Iphone Application', 'Develop An Iphone Application'), ('Develop an Android Application', 'Develop an Android Application'), ('Laravel PHP Project', 'Laravel PHP Project'), ('Ios And Android', 'Ios And Android')]), ('Designers & Creatives', [('Design A Website Mockup', 'Design A Website Mockup'), ('Design Some Icons', 'Design Some Icons'), ('Design A Banner', 'Design A Banner'), ('Re-design BoonTech website', 'Re-design BoonTech website'), ('Design a Logo', 'Design a Logo'), ('Photo backgrounds remove', 'Photo backgrounds remove'), ('Creative Design', 'Creative Design'), ('Business card design', 'Business card design'), ('Create Videos for FB and Google Ads', 'Create Videos for FB and Google Ads')]), ('Content Writers', [('Content Writing', 'Content Writing'), ('Write A Book', 'Write A Book'), ('Academic Writing', 'Academic Writing'), ('This is the internship report for the students of undergraduate', 'This is the internship report for the students of undergraduate'), ('Proofreading and editing', 'Proofreading and editing')]), ('Virtual Assistants', [('Install Something At My Home', 'Install Something At My Home'), ('Take Some Photos', 'Take Some Photos'), ('BPO', 'BPO'), ('Data entry', 'Data entry'), ('A virtual Assistant to enter finance information', 'A virtual Assistant to enter finance information')]), ('Customer Service Agents', [('Pickup Or Deliver Something', 'Pickup Or Deliver Something'), ('Clean My House Or Business', 'Clean My House Or Business'), ('Customer support', 'Customer support')]), ('Sales & Marketing Experts', [('Assist Me With Bulk Marketing', 'Assist Me With Bulk Marketing'), ('Telemarket For Me', 'Telemarket For Me'), ('Build Links To My Website', 'Build Links To My Website'), ('Search Engine Marketing PPC Expert', 'Search Engine Marketing PPC Expert'), ('Promotion', 'Promotion'), ('Email marketing campaign', 'Email marketing campaign')]), ('Accountants & Consultants', [('Find An Accountant', 'Find An Accountant'), ('Assist With Project Management', 'Assist With Project Management'), ('Write A Patent', 'Write A Patent')]), ('Video and Animation', [('Whiteboard & Animated Videos', 'Whiteboard & Animated Videos'), ('Intros & Animated Logos', 'Intros & Animated Logos'), ('Promotional Videos', 'Promotional Videos'), ('Editing & Post Production', 'Editing & Post Production'), ('Lyrics & Music Videos', 'Lyrics & Music Videos'), ('Spokesperson Videos', 'Spokesperson Videos'), ('Animated Characters & Modeling', 'Animated Characters & Modeling'), ('Short Video Ads', 'Short Video Ads'), ('Live Action Explainers', 'Live Action Explainers'), ('Others', 'Others')]), ('Data Science and Analytics', [('Data Science & Analytics', 'Data Science & Analytics'), ('A/B Testing', 'A/B Testing'), ('Data Visualization', 'Data Visualization'), ('Data Extraction / ETL', 'Data Extraction / ETL'), ('Data Mining & Management', 'Data Mining & Management'), ('Machine Learning', 'Machine Learning'), ('Quantitative Analysis', 'Quantitative Analysis'), ('Other - Data Science & Analytics', 'Other - Data Science & Analytics')]), ('Legal', [('Legal', 'Legal'), ('Contract Law', 'Contract Law'), ('Corporate Law', 'Corporate Law')]), ('Programming and Technology', [('Fun and Lifestyle', 'Fun and Lifestyle')]), ('Fun and Lifestyle', [('design iron and wood 31', 'design iron and wood 31'), ('fashion', 'fashion'), ('Others', 'Others')]), ('Engineering and Architecture', [('Engineering and Architecture', 'Engineering and Architecture'), ('3D Modeling and CAD', '3D Modeling and CAD'), ('Architecture', 'Architecture'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil & Structural Engineering', 'Civil & Structural Engineering'), ('Contract Manufacturing', 'Contract Manufacturing'), ('Electrical Engineering', 'Electrical Engineering'), ('Interior Design', 'Interior Design'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Product Design', 'Product Design'), ('Other', 'Other')]), ('Other', 'Other')], default='other', max_length=80),
        ),
    ]
