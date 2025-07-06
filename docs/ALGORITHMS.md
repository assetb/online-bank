# Algorithm Overview

This document summarizes the basic flows described in the technical specification.

## User Registration
1. User sends personal data to the bot.
2. Service stores the data and requests KYC verification.
3. On success the user proceeds to card issuance.

## Card Issuance
1. Verified user requests a new card with promo code.
2. Gateway calls Card Service which interacts with BinCentric API.
3. Card details are returned and shown in the mini app.

## Card Funding
1. User selects funding method and amount.
2. Gateway creates a transaction via Transaction Service.
3. Service communicates with BinCentric and notifies the bot on completion.

Refer to `TD.txt` for the full Russian version of the specification.
