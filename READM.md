# Understand file structure
```firstname-lastname/ ``` <br>
```├── task1/```<br>
```│ ├── expectations.txt # expect output task1```<br>
```│ ├── solution.py  # analyse_sales```<br>
```│ └── sales.csv    # your sample data file```<br>
```├── task2/```<br>
```│ ├── expectations.txt # expect output task2```<br>
```│ └── solution.py  # classify_sentiments```<br>
```├── task3/```<br>
```│ ├── expectations.txt # expect output task3```<br>
```│ ├── solution.py  # run_pipeline```<br>
```│ └── reviews.csv  # your sample data file```<br>
```└── README.md      # optional: notes or assumptions```<br>

# Git repo: <br>
```https://github.com/sassdahRAK/Techpreneur-2.0-Application-Exercise.git```<br>

> Clone Repo <br>
```git clone https://github.com/sassdahRAK/Techpreneur-2.0-Application-Exercise.git```

# Note: SUBMISSION STRUCTURE <br>
1. a single .zip file named firstname-lastname.zip. <br>
2. Before zipping: confirm all solution.py files can be imported without errors. <br>
3. Do not hard-code file paths — use the filepath argument. <br>
4. Store your HF_API_TOKEN in a .env file locally but do not include it in the zip. <br>

> Academic integrity: All submissions are compared against each other and checked for similarity. If identical or near-identical solutions are found, both will receive a score of zero. <br>

# Methodology  <br>
1. Python 3.10+  <br>
2. See allowed libraries per task  <br>
3. Work independently  <br>
> Use clean, readable code throughout  <br>
> single-letter variable names  <br>
> uncommented logic will be penalised.  <br>

# Recording time
H:2:20-3:12 Sun: session1 - organize file structure. <br>
H:8:27-8:35 Mon: session2 - start work on task1 <br>
H:3:50-5:26 Mon: session3 - still work on task1 <br>
H:4:10-7:13 Tue: session4 - still work on task1 <br>

# Referrences 
> Officail Source: <br>
> 1. Pandas document: https://pandas.pydata.org/docs/user_guide/10min.html#basic-data-structures-in-pandasn <br>
> 2. Python HTTP client documentation: https://docs.python.org/3/library/http.client.html <br>
> 3. 
> Non-Officail Source: <br>
> 1. Can I create http request in python? https://www.google.com/search?q=can+python+create+http+request&rlz=1C5CHFA_enKH1081KH1081&oq=can+python+create+http+request&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyCggFEAAYgAQYogQyBwgGEAAY7wUyCggHEAAYgAQYogQyCggIEAAYogQYiQXSAQkyMDQ1NGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8 <br>
> 2. Read csv and file path: https://www.google.com/search?q=how+to+give+the+path+.csv+to+.py+file+in+the+same+subfolder&rlz=1C5CHFA_enKH1081KH1081&oq=how+to+give+the+path+.csv+to+.py+file+in+the+same+subfolder&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigAdIBCTM4ODM1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8 <br>
> 3. secure token handling: https://www.google.com/search?q=Do+not+hard-code+file+paths+%E2%80%94+use+the+filepath+argument.+Store+your+HF_API_TOKEN+in+a+.env+file+locally+but+do+not+include+it+in+the+zip.&rlz=1C5CHFA_enKH1081KH1081&oq=Do+not+hard-code+file+paths+%E2%80%94+use+the+filepath+argument.+Store+your+HF_API_TOKEN+in+a+.env+file+locally+but+do+not+include+it+in+the+zip.&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAjIHCAIQIRiPAjIHCAMQIRiPAtIBCDEyOTBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8 <br>
> 4. 

# Learning outcome
> What Is an API Token? <br>
> API tokens are small snippets of code built to secure API access. These small strings are sent to API servers, where they act as identification, proving whether the user or application has access to the API. Their purpose is to give the API server both information and authentication. <br>

> How API Tokens Work? <br>
> Here's what happens when a token is used:
> A user or application trying to connect with the API provides the token to the API server to authenticate their identity and access. 
> The server reviews the token. If the token is valid, the API server grants the requested level of access. If the token is invalid or does not grant the necessary level of access, the API server rejects the request.
>When using API tokens, the API provider can adjust or revoke access at any time. API tokens can even have built-in expiration dates, so they can't be reused forever. <br>

> API Token Anatomy <br>
> API tokens are typically composed of three parts: a header, a payload, and a signature.
> - Header: <br>
> The header contains information about the token, like the token type and algorithm used to generate the signature. <br>
> - Payload:<br>
> The payload contains more sensitive information about the individual user or application. This might include user IDs, access permissions, and other authentication data. <br>
> - Signature: <br>
> The signature protects the token from tampering. By using cryptographic algorithms to generate a unique, secure signature for each token, APIs can validate the data transmitted between systems. <br>

>API Token vs. API Key <br>
>It's easy to get API tokens and API keys mixed up. Especially since they're both used for granting access to an API and both are in the HTTP headers of an API request. But they have different purposes. In fact, they're often used together because they complement each other. <br>

>An API key is used to keep anonymous traffic out — that's helpful for API security because malicious actors like to hide in anonymous traffic. And API keys can do some broad authorization too. But they don't provide rigorous security. <br>

> API Key <br>
> - Prevents anonymous traffic <br>
> - Authenticates projects, not individuals or applications <br>
> - Is simpler to implement <br>
> - Is used for public APIs or APIs that don't demand strict user authentication <br>

> API Token <br>
> - Authenticates users and applications <br>
> - Is used for API security <br>
> - Can be managed by API provider <br>
> - Can include a built-in expiration date <br>

> Types of API Tokens <br>
> Much like different APIs use different API protocols, API tokens come in different types too. Each type of API token has its own strengths and weaknesses in terms of security and ease of implementation. <br>

> JSON Web Tokens
> - Possibly the most well-known API token type, JSON web tokens are used everywhere. As compact, self-contained tokens, JSON web tokens contain all the information needed about the user or application.
> - They're also URL-safe, which makes them a particularly useful type of token for web applications because they can be used in a URL.
> - These web tokens can include extra security features as needed. It's also possible to add extra information to these tokens, a useful feature for developers.

> OAuth Tokens
> - Another common API token, OAuth tokens are used for delegated authorization. This means that they allow a user to provide a third-party application access to their resources without needing to give the third-party application access to the user's login credentials.
> - OAuth tokens are an invaluable security addition used for web applications and APIs that require user authentication and authorization, like social media platforms or online banking.>

> Personal Access Tokens: 
> As the name suggests, personal access tokens are tied to a personal account and individual credentials. They allow users to provide a third-party application access to one service. Users can directly access their own resources via third-party apps when using personal access tokens.

> Bearer Tokens: 
> A simpler authentication token than the others, bearer tokens function without additional cryptographic operations. Because of this, they're not as secure as the others. But they're easier to implement. Like other types of tokens, though, they're self-contained, so they have all the information they need to access the API inside. 

> Single Sign-On (SSO) Tokens:
> This token is usually issued by a third-party identity provider (IdP) rather than the API provider itself. SSO tokens authenticate once with IdP, then have access to multiple applications without the need for re-authentication each time. 

> API Token Security
> API tokens are considered to be one of the most secure methods of authentication, as they deliver an added layer of security compared to API keys. To maintain this high level of security, the API token use has to be monitored. This involves implementing strict access controls and regularly updating the tokens or adding expiration dates to keep them from becoming compromised over time. If the API provider notices suspicious usage patterns, they'll revoke access to that user or application. 

> Developers use several methods to keep API tokens secure.
> - Encryption and Hashing Algorithms <br>
> Strong encryption and hashing algorithms are key components of secure API token management. 
> - - Encryption algorithms, like AES-256, are used to ensure that API tokens are transmitted securely and cannot be intercepted or tampered with by third parties.
> - - Hashing algorithms, such as SHA-256, are used to ensure that API tokens cannot be easily reverse-engineered or guessed by attackers.
> - IP Address Management
> - - By restricting access to specific IP addresses, API providers block unauthorized users and applications, keeping data safe and preventing malicious attacks.
> - - To manage IP addresses associated with API tokens, API providers typically require users or applications to specify a list of allowed IP addresses when creating or requesting a token. The API server validates the IP address of incoming requests against the list of allowed IP addresses and only grants access if the IP address is on the list.
> - Limited End-user Access
> - - API tokens are configured to grant access only to the specific resources and actions that are required for a particular use case. For example, if an API is used to manage a user's financial data, the API token should only grant access to the specific types of financial data that are required and should restrict access to any other data or resources. This keeps user data protected.
> - SSL Attack Prevention
> - - SSL prevents man-in-the-middle attacks — where a third party intercepts and alters the communication between the client and server. Without SSL encryption, the API traffic can be intercepted, potentially exposing sensitive data and compromising the system.
> - - Implementing SSL encryption for API traffic typically involves obtaining an SSL/TLS certificate and configuring the API server to use HTTPS, the encrypted version of HTTP.
> - - SSL encryption also improves the performance of the API by reducing the time required to establish a secure connection and the impact of network latency on API performance.

