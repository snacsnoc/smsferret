# smsferret - SMS to DuckDuckGo 

Have you ever been in the middle of nowhere with limited connectivity and wanted to look something up? smsferret was created for instances where data is limited when a cellular connection exists. Loading a webpage under such conditions is unusable for such a small amount of data requested. 

smsferret is a SMS to search engine (DuckDuckGo) bridge. 

We can text our Twilio phone number and receive a search engine result. Most North American carriers support SMS concatentation, which allows message of up to 1600 characters. In the header of the first SMS, it tells us how many parts there are, and reassembles the SMS in order on the user's device. smsferret does not do this.

Under limited connectivity, we want to split our text messages up to increase deliverability (eg, one 1500 characters SMS vs two 160 character SMS). 



Install requirements:
`pip install Flask`

`pip install duckduckgo_search`

`pip install twilio`

Start Flask app:
` python3 -m flask run --host=0.0.0.0`

Create your messaging app on Twilio, enter the Flask URL as request webhook URL.

### Reading


https://support.twilio.com/hc/en-us/articles/223181508-Does-Twilio-support-concatenated-SMS-messages-or-messages-over-160-characters-


https://help.goacoustic.com/hc/en-us/articles/360043843154--How-character-encoding-affects-SMS-message-length

### Tools

https://www.developershome.com/sms/gsmAlphabet.asp

https://twiliodeved.github.io/message-segment-calculator/