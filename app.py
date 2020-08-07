#!/usr/bin/env python3

from aws_cdk import core

from sonar.sonar_stack import SonarStack


app = core.App()
SonarStack(app, "sonar")

app.synth()
