import os
import json
#import logging

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
translate = boto3.client('translate')


def translateText(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

   # translate = boto3.client(service_name='translate', region_name='region', use_ssl=True)

   # result2 = translate.translate_text(Text="Hello, World", SourceLanguageCode="en", TargetLanguageCode="de")
    #print('TranslatedText: ' + result2.get('TranslatedText'))
    #print('SourceLanguageCode: ' + result2.get('SourceLanguageCode'))
    #print('TargetLanguageCode: ' + result2.get('TargetLanguageCode'))
    #traduction = translate.translate_text(Text=result.Text, SourceLanguageCode=auto, TargetLanguageCode=languages)  
	#logging.info("Translation output: " + str(result.text))
	
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
