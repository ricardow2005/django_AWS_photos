from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Amazon s3
import boto3



def index(request):

    s3 = boto3.resource('s3', verify=False,
         aws_access_key_id='AKIA3TLNW7VUGMTP3UGK',
         aws_secret_access_key= 'EZydBtFjABypJIrQr4pqHa2qsw55ytzH68GDQaGi')
    bucket = s3.Bucket('photo-tools-rwalter')
    #objs = bucket.meta.client.list_objects(Bucket='photo-tools-rwalter')
    for f in bucket.objects.all():
        print(f.key)


    template = loader.get_template('photos/index.html')
    return HttpResponse(template.render())
    #return HttpResponse("Teste")
