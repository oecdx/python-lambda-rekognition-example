import io
import boto3
import base64
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Lambda handler
    """
    LOGGER.info("event - %s", event)

    try:

        results = rek_faces(event["body-json"])

        return {
            "results": results
        }

    except Exception as exception:
        LOGGER.error("Exception:%s", exception)
        LOGGER.error("handling failed.")
        return {}


def convert_b64_string_to_bynary(s):
    """base64をデコードする"""
    return base64.b64decode(s.encode("UTF-8"))


def rek_faces(data):

    if 'image' in data:
        # for aws
        rekognition = boto3.client('rekognition')

        req_image = convert_b64_string_to_bynary(data['image'])

        image_bin = io.BytesIO(req_image)
        image = image_bin.getvalue()
        response = rekognition.detect_faces(
            Image={'Bytes': image}, Attributes=['ALL'])
        if response and 'FaceDetails' in response:
            data['FaceDetails'] = response['FaceDetails']

        return data

    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return {}
