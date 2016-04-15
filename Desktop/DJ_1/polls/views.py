import random
import requests
import datetime
import  urllib2
from django.contrib.sites import requests
from django.http import HttpResponse
from django.template.response import TemplateResponse

url0 = "http://api.mVaayoo.com/mvaayooapi/MessageCompose?user=Blazemits@gmail.com:blazemits123&senderID=TEST SMS&receipientno="
url1 = "&dcs=0&msgtxt="
url2 = "&state=4"



def current_datetime(request):
    dyn_data_str = "This is a Dynamic data string"
    otp_gen = random.randint(100000, 999999);
    new_otp = str(otp_gen);
    url = url0 + url1 + url2 + new_otp;
    return TemplateResponse(request, "index.html", {"what_ever": url, "otp": otp_gen})


def input_data(request,num):
    otp_gen = str(random.randint(100000, 999999));
    url = url0 +num+ url1 +"Your Test OTP is "+otp_gen+num+url2
    now = datetime.datetime.now()
    html1 = "<html><body>It is now %s.</body></html>" % url
    reqst=urllib2.Request('http://api.mVaayoo.com/mvaayooapi/MessageCompose?user=Blazemits@gmail.com:blazemits123&senderID=TEST SMS&receipientno=8137020996&dcs=0&msgtxt=This is Test message&state=4')
    #requests.get('http://api.mVaayoo.com/mvaayooapi/MessageCompose?user=Blazemits@gmail.com:blazemits123&senderID=TEST SMS&receipientno=8137020996&dcs=0&msgtxt=This is Test message&state=4')
    response=urllib2.urlopen(reqst)
    html=response.read()
    return  HttpResponse(html)