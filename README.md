# StreamSummaryMaker
Youtube Stream Summary Maker


#### main data flow
- ccparser.py  ─ text_analyzer.py
-              └ savior.py


#### Descriptions
- ccparser.py       : get json data from one youtube url using "youtube_transcript_api"
- text_analyzer.py  : make wordcloud or statistics kinda things.
- savior.py         : save json data from cc parser.py. (For text dataset)
- test.py           : for test.
- main.py           : main API