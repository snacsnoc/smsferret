#!/usr/bin/python3

# 
# smsferret (https://github.com/snacsnoc/smsferret)
#
# Copyright (c) 2022 Easton Elliott
# 
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from duckduckgo_search import ddg


def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [
        item_to_replace_with if item == item_to_replace else item
        for item in list_to_replace
    ]


app = Flask(__name__)


@app.route("/sms", methods=["GET", "POST"])
def incoming_sms():

    body = request.values.get("Body", None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Perform our DDG search
    results = ddg(body, region="wt-wt", safesearch="Moderate", time="y", max_results=5)

    if results is not None:

        #Remove leading and trailing whitespace to reduce character count
        first_result_title = results[0]["title"].replace(
            " ", ""
        )  

        first_result_body = results[0]["body"]  

        # Our concatentated search result
        line = first_result_title + first_result_body

        # Replace two byte characters
        line = replace_values(line, "~", "#")

        # Change our list to a string
        line = "".join(line)


        # Characters to cut by
        n = 160

        # split into 160 segments
        for i in range(0, len(line), n):
            print(str(i) + ": " + line[i : i + n])
            print(len(line[i : i + n]))
            resp.message(line[i : i + n])

        return str(resp)

    else:
        resp.message("invalid results")
        return str(resp)
 


if __name__ == "__main__":
    app.run(debug=True)
