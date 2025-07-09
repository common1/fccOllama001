# fccOllama001

## See also:

API Endpoints
[http://github.com/ollama/ollama/blob/main/docs/api.md]

Ollama API Usage Examples
[https://www.gpu-mart.com/blog/ollama-api-usage-examples]

## 01 Download Ollama Locally

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=1083s]

## 02 Ollama Models - How to Pull Different Ollama Models Locally
```
$ ollama run llama3.2
>>> /bye
$ ollama run llama3.2:1b
>>> /?
>>> /bye
$ ollama list
```
## 03 LLM Parameters Deep Dive

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=2021s]

## 04 Understanding Model Benchmarks

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=2379s]

## 05 Ollama Basic CLI Commands - Pull and Testing Models

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=2576s]

```
$ ollama list
$ ollama help
$ ollama rm llama3.2:1b
$ ollama pull codegemma:2b
$ ollama run codegemma:2b
>>> /bye
$ ollama rm codegemma:2b
```
## 06 Pull in the Llava Multimodal MOdel and Captioning an Image - Hands-on

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=2829s]

[https://github.com/pdichone/ollama-fundamentals]

```
$ ollama run llava:7b
>>> what is in this image ./flower_1.png
...
>>> and now write me a short poem about that
...
>>> tell me more about those flowers
```

## 07 Summarize and Sentiment Analysis and Customizing Models with the Modelfile

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=3133s]

```
$ ollama run llama3.2
>>> what is the sentiment of the following sentence "I am not willing to pay you back"
>>> /bye

$ ollama create james -f ./Modelfile
$ ollama run james
>>> What is your name
>>> Are you smart
>>> /bye
$ ollama rm james
```

## 08 Ollama REST API

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=3602s]

[http://localhost:11434/]

```
$ curl "http://localhost:11434/api/generate" -d '{
"model": "llama3.2",
"prompt": "Tell me a fun fact about Portugal",
"stream": false
}'

$ curl "http://localhost:11434/api/chat" -d '{
"model": "llama3.2",
"messages": [{"role": "user", "content": "tell me a fun fact about Mozambique"}],
"stream": false
}'
```

## 09 Ollama REST API - Request JSON

```
$ curl "http://localhost:11434/api/chat" -d '{
"model": "llama3.2",
"messages": [{"role": "user", "content": "tell me a fun fact about Mozambique"}],
"stream": false
}'

$ curl "http://localhost:11434/api/generate" -d '{
"model": "llama3.2",
"prompt": "What color is the sky at different times of the day? Respond using JSON",
"format": "json",
"stream": false
}'
```

## 010 Ollama Models Support Different Tasks - Summary

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=4079s]

## 011 Different Ways to Interact with Ollama Models - Overview

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=4120s]

[https://msty.app/]

[https://assets.msty.app/prod/latest/linux/amd64/Msty_amd64_amd64.deb]

```
Download and install
$ chmod a+x Msty_amd64_amd64.deb
$ sudo apt install ./Msty_amd64_amd64.deb
$ sudo chown root:root /opt/Msty/chrome-sandbox
$ sudo chmod 4755 /opt/Msty/chrome-sandbox

```
## 012 Introduction to Python Library for Building LLM Applications Locally - Part 1

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=4906s]

```
$ pip install requests
```
## 013 Interact with Llama3 in Python using Ollama REST API

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=5054s]

## 014 Ollama Python Library Chatting with our Model - Part 1

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=5369s]

```
$ pip install ollama
```

## 014 Ollama Python Library Chatting with our Model - Part 2

...

## 015 Chat Example with Streaming

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=5742s]

## 16 Using Ollama Show Function

[https://www.youtube.com/watch?v=GWB9ApTPTv4&t=5835s]

