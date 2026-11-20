# Alex — Python Voice Assistant

A desktop Python assistant with microphone input and text-to-speech. Supports time, opening sites, web search, Wikipedia summaries, local music, note taking and in-process reminders.

## Run
```bash
python -m pip install -r requirements.txt
python assistance.py
```

Requires a working microphone and speakers. Speech recognition and Wikipedia access may need internet. Say "Alex", followed by commands such as "time", "open github.com", "search machine learning", "note buy milk" or "remind me in 5 minutes take a break".

## Files
- `assistance.py`: complete Python application
- `requirements.txt`: dependencies

**Limitations:** Reminders run only while the script remains open. This is a fixed-command assistant, not an LLM chatbot. Online recognition sends speech audio to a third-party service.

Author: Mohsin Atta
