# findingYOurTop5Resources_inAWS

I made this script at work while working on FinOps tasks. See, in Azure they make things simple for you, by providing charts that can make life easy for clients to understand what is going on, however in aws, the charts are not as friendly to people are are not technical. Therefore, I have created this script that will generate a chart using the data of your account in scope, and than download the chart generated as a png file. 

Before running this script in the aws cli, you need to install a python library that will help create this image, named matplot:
pip install --user boto3 matplotlib

Than, upload the script I have provided, and run it:
python top_aws_services.py
