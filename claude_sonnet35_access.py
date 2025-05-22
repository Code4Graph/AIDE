import boto3
import json
import logging
from boto3 import client
from botocore.config import Config
from botocore.exceptions import ClientError
from PyAwsHelper.boto_helper import BotoHelper
import time

# Claude v3
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_message(bedrock_runtime, model_id, system_prompt, messages, max_tokens):
    response = bedrock_runtime.converse(
        modelId=model_id,
        system=[{"text": system_prompt}],
        messages=[{"role": "user", "content": [{"text": messages[0]["content"]}]}],
    )
    response_body = response.get("output").get("message")
    return response_body


def get_claude_response(system_prompt, prompt):
    """
    Entrypoint for Anthropic Claude message example.
    """
    while True:
        try:
            config = boto3.session.Config(
                connect_timeout=300,
                read_timeout=300,
                retries={"max_attempts": 3, "mode": "standard"},
                max_pool_connections=16,
            )
            bedrock_runtime = BotoHelper().get_client(
                service_name="bedrock-runtime",
                region_name="us-west-2",
                config=config,
                role_arn="arn:aws:iam::533266999589:role/invoke-bedrock-api",
            )
            model_id = "us.anthropic.claude-3-5-sonnet-20240620-v1:0"
            system_prompt = system_prompt
            max_tokens = 200

            user_message = {"role": "user", "content": prompt}
            messages = [user_message]
            response = generate_message(
                bedrock_runtime, model_id, system_prompt, messages, max_tokens
            )
            output = response["content"][0]["text"]
            return output

        except ClientError as err:
            message = err.response["Error"]["Message"]
            logger.error("A client error occurred: %s", message)
            print("A client error occured: " + format(message))
            print("Retry!")
            time.sleep(10)
