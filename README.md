Streamlit Examples
===

Streamlit is a faster way to build and share data apps. Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required. 

This repo contains series of example Python code provides you a step-by-step progress to learn to use Streamlit to build your application. 

## Prequesites
1. You know how to set a Python environment, you can use virtualenv(aka venv), pyenv, or conda to create it.
2. Start from #3 example, it will use LLM(Large Language Model) from Amazon Bedrock. Please make sure you enabled models from Amazon Bedrock. Recommend to use `us-east-1` region.
3. You have AWS profile/credentials setup. In some example, I will use a profile in my local called `us-east-1`. You can use your preferred profile name and simply change it. Or use the `dotenv` to setup.

## Setup
Assume you have Python environment setup.
1. Install Python libraries
```
pip install -r requirements.txt
```
2. Prepare your AWS credentials / Profile
```
cp env-example .env
```
modify the `.env` accordingly to make sure you have necessary permissions.

## Run
You can run the code one by one, each one is an independent Streamlit app.
```
streamlit run xxx.py  
```
