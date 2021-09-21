#!/usr/bin/env python3

from aws_cdk import core

from config_chatbot.config_chatbot_stack import ConfigChatbotStack

app = core.App()
ConfigChatbotStack(app, "config-chatbot")

app.synth()
