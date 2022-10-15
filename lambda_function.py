import json
import boto3
client_sentiment = boto3.client("comprehend")

def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    if http_method == 'POST':
        body = event.get('body')
        comment = ''
        if body is not None:
            comment = json.loads(body).get('comment',comment)
    
   
        response  = client_sentiment.detect_sentiment(
            Text = comment,
            LanguageCode = "en" 
            )
    # print(response)
    # translate = boto3.client(
    #     service_name = "translate",
    #     region_name = "ap-south-1",
    #     use_ssl = True
    #     )
    # result = translate.translate_text(
    #     Text = text,
    #     SourceLanguageCode = "en",
    #     TargetLanguageCode = "de"
                
    # )
    # print('TranslatedText : ' + result.get('TranslatedText'))
    # print('SourceLanguageCode : ' + result.get('SourceLanguageCode'))
    # print('TargetLanguageCode : ' + result.get('TargetLanguageCode'))
    # # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        # 'Translated':result.get('TranslatedText'),
        # 'Response':response
    }
