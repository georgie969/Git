AWS Config helps to implement compliance within an organization's IT infrastructure. This Solution helps to easily provide users with information about non-compliant resources in order to take neccessary action improve security posture. The information is sent directly to a Slack Channel for immediate action and response by all concerned parties. This removes the need to constantly search the Console for Non-compliant resources as the information comes directly to you via Slack.

This is a CDK Template to create a new AWS ChatBot to automatically deploy an AWS Managed Config rule as well as a Chatbot solution to notify users when a Config rule is Non compliant/Compliant via sending notifications to a Slack Channel linked to the AWS Chatbot

This project will create the following resources in your AWS cloud environment:

    Deploys 2 AWS Managed Config rules - S3_BUCKET_VERSIONING_ENABLED and EC2_VOLUME_INUSE_CHECK
    Creates an AWS ChatBot with a Slack Channel
    Subscribes the SNS Topic to the Slack Channel

Requirements:

    AWS CLI
    AWS CDK
    Python 3.x
    AWS account to create resources listed above
    Config Service activated within your account
    An SNS Topic subscription attached to AWS Config within your console
    A Slack account and Channel
    A Configured AWS ChatBot with a Slack workspace

Helpful links:

    How to create an SNS Topic: https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html
    How to set up your SNS Topic with AWS Config: https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html
    How to set up AWS Chatbot with Slack: https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html

Libraries to be installed and how to install them. 

The AWS CDK comes with a library of constructs called the AWS Construct Library which is divided into modules, one for every AWS service. 
For this project we will use pip install to install modules we need and all it’s dependencies.

Installation Commands:

pip install aws_cdk.aws_chatbot
pip install aws_cdk.aws_config
pip install aws_cdk.aws_events_targets
pip install aws_cdk.aws_sns

This project was inspired by the AWS CDK workshop (https://cdkworkshop.com) and I highly recommend you go through it before utilizing this CDK template if you have no prior experience with using AWS CDK.

This project is set up like a standard Python project. The initialization process also creates a virtualenv within this project, stored under the .env directory. To create the virtualenv it assumes that there is a python3 (or python for Windows) executable in your path with access to the venv package. If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux, you will want to create a project directory:

$ mkdir ~/cdk-samples

Now you are ready to create a virtualenv:

$ cd ~/cdk-samples
$ python3 -m venv .env

After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.

$ source .env/bin/activate

If you are a Windows platform, you would activate the virtualenv like this:

% .env\Scripts\activate.bat

Once the virtualenv is activated, you can install the required dependencies.

$ pip install -r requirements.txt

Then install the other required dependencies indicated in the requirements.txt file

Install the latest version of the AWS CDK CLI:

$ npm i -g aws-cdk

At this point you can now synthesize the CloudFormation template for this code.

$ cdk synth

Deploy

Run "cdk bootstrap" and then run "cdk deploy". This will deploy / redeploy your Stack to your AWS Account.

To clean up, issue this command:

$ cdk destroy

To exit the virtualenv python environment:

$ deactivate