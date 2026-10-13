# Messenger Sales Bot

A small Flask webhook prototype for a computer sales and spare-parts chatbot. The project was originally written in 2021 and connects incoming Facebook Messenger events to a simple rule-based reply flow.

## What it does

- Provides a webhook route at `/` for verification and incoming Messenger events.
- Replies to a small set of greetings and product requests.
- Includes example keyboard-brand names and prices.
- Sends replies through the Facebook Messenger Platform Graph API.

This is an educational prototype, not a production-ready chatbot.

## Project files

| File | Purpose |
|---|---|
| `app.py` | Flask webhook and basic keyword-based conversation logic. |
| `bot.py` | Helper that sends text messages to the Messenger Graph API. |
| `requirements.txt` | Python package dependencies. |

## Requirements

- Python 3
- A Meta/Facebook app configured for Messenger
- A Facebook Page and a Page Access Token
- A publicly reachable HTTPS endpoint for webhook use

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Before running the webhook, edit `app.py`:

1. Replace `YOUR_ACCESS_TOKEN` with the Page Access Token for your Messenger app.
2. Replace the verification value `secret` with a private verification token, and use the same value when configuring the webhook in Meta.

Do not commit real access tokens or other credentials to a public repository. This prototype currently stores these values in source code; move them to environment variables before deployment.

## Run locally

Start the Flask development server:

```bash
python app.py
```

The server listens on Flask's default local address. A Messenger webhook needs an HTTPS URL reachable by Meta; for local development, configure a secure tunnel and use its HTTPS URL in the Meta webhook settings.

## Example conversation

The intended basic interaction is:

1. A user greets the bot.
2. The bot asks what product they need.
3. The user requests a keyboard, mouse, or RAM.
4. The bot asks for a company.
5. The bot replies with a sample price.

The current implementation does not reliably complete every step; see the limitations below.

## Known limitations

- The webhook assumes a particular JSON structure and does not validate malformed or unsupported events.
- Incoming text matching is exact and case-sensitive.
- The company checks use chained comparisons that do not match the intended company-name checks, so the listed price replies are not reached as intended.
- Prices are integers, while Messenger message text should be a string.
- The API URL is modified during each send; repeated sends through one `Bot` instance can target a malformed URL.
- API requests have no timeout or explicit failure handling.
- The webhook does not validate Meta's request signature.
- The webhook verification token and Page Access Token are not loaded from secure configuration.
- The application entry point enables Flask debug mode; do not expose this configuration on an internet-facing deployment.
- The Graph API version in the original code is `v13.0` and may need updating to a version supported by Meta.

## Before deployment

Treat this repository as a historical learning project. Fix the limitations above, configure secrets outside source control, disable debug mode, and test against the current Messenger Platform API before deploying.

## License

No license is included. Contact the author before reusing or redistributing this code.
