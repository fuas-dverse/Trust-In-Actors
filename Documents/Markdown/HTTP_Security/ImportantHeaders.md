# Important HTTP Security Headers

Based on the other markdown file, I will rank the headers on what is most likely the most important and how it can be implemented in the current know languages (Python and Next.js).

Aside of which ones are the likeliest to be important it, I also base it around what you can do with it. Should be implemented at the top and what needs to be removed at the bottom.

Although every header should be implemented. I recommend that you at least do it till Set-Cookie as till then it will be things that you should self implement with a high importance of security.  
I recommend that Content-type and Strict-Transport-Security should be implemented for every actor in the DVerse project.

## Content Security Policy (CSP)

Content Security Policy is important because this deals with a lot of the security issues like where it can load resources from or that it needs to block/prevent the user agent from loading mixed content.

Look through [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) for a more clear understanding of all possible options.

The following block only allows scripts only from the same origin ('self') and also allow inline scripts ('unsafe-inline').

Python:

````python
csp_header = {
    'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline';"
}
connection = requests.get('example.com', headers=csp_header)
````

For Next.js it will be easier to look at: <https://nextjs.org/docs/app/building-your-application/configuring/content-security-policy>

The following is the most important part of the document. In this it achieves for each request to a page. I do recommend with Nonces as it says in the document that there are legitimate scenarios where inline scripts are necessary.

TypeScript:

````TypeScript
import { NextRequest, NextResponse } from 'next/server'
 
export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`
  // Replace newline characters and spaces
  const contentSecurityPolicyHeaderValue = cspHeader
    .replace(/\s{2,}/g, ' ')
    .trim()
 
  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)
 
  requestHeaders.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )
 
  const response = NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  })
  response.headers.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )
 
  return response
}
````

## Permission-Policy

I think this is important because with this you can  disable browser features.  
You can control it so which origins can use which browser features, both in the top-level page and in embedded frames.

This helps prevent that an injection, for example an XSS, enables the camera, the microphone, or other browser feature.

Python:

````Python
pp_header = {  'Permissions-Policy': 'geolocation=(), microphone=()'}

response = requests.get('example.com', headers=pp_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Permissions-Policy',
            value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
            }
        ]
    ]
````

## Strict-Transport-Security (HSTS)

This transport header lets a website tell browsers that it should only be accessed using HTTPS, instead of using HTTP.

You should note that you need to read carefully how this header works before using it. If the HSTS header is misconfigured or if there is a problem with the SSL/TLS certificate being used, legitimate users might be unable to access the website.

For more information about this you can go to the following cheat sheet: [HTTP Strict Transport Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)

Python:

````Python
http_header = {  'Strict-Transport-Security: max-age=63072000; includeSubDomains; preload'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Strict-Transport-Security',
            value: 'max-age=63072000; includeSubDomains; preload'
            }
        ]
    ]
````

## X-Content-Type-Options

The X-Content-Type-Options response HTTP header is used by the server to indicate to the browsers that the MIME types advertised in the Content-Type headers should be followed and not guessed.

This header is used to block browsers' MIME type sniffing, which can transform non-executable MIME types into executable MIME types (MIME Confusion Attacks).

Python:

````Python
http_header = {  'X-Content-Type-Options: nosniff'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
            }
        ]
    ]
````

## Content-Type

The Content-Type representation header is used to indicate the original media type of the resource (before any content encoding is applied for sending). If not set correctly, the resource (e.g. an image) may be interpreted as HTML, making XSS vulnerabilities possible.

Recommended is to set the `charset` attribute to prevent XSS in HTML pages. While `text/html` or other possible MIME types needs to be included to set the Content-Type.

Set to `Content-Type: text/html; charset=UTF-8` for messages.

Python:

````Python
http_header = {  'Content-Type: text/html; charset=UTF-8'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
export default async function handler(req, res) {
    const data = { message: 'Hello, Next.js!' };

    // Set the Content-Type header to application/json
    res.setHeader('Content-Type', 'application/json');

    // Send the data as a JSON response
    res.status(200).json(data);
}
````

## Referrer-Policy

The Referrer-Policy HTTP header controls how much referrer information (sent via the Referrer header) should be included with requests.  Aside from the HTTP header, you can also [set this policy in HTML](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#integration_with_html).

The default behavior in modern browsers is to no longer send all referrer information (origin, path, and query string) to the same site but to only send the origin to other sites. However, since not all users may be using the latest browser its suggested that you force this behavior by sending this header on all responses.

Python:

````Python
http_header = {  'Referrer-Policy: strict-origin-when-cross-origin'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Referrer-Policy',
            value: 'strict-origin-when-cross-origin'
            }
        ]
    ]
````

## X-XSS-Protection

The HTTP X-XSS-Protection response header was a feature of Internet Explorer, Chrome and Safari that stopped pages from loading when they detected reflected cross-site scripting (XSS) attacks. These protections are largely unnecessary in modern browsers when sites implement a strong Content-Security-Policy that disables the use of inline JavaScript ('unsafe-inline').

Even though this header can protect users of older web browsers that don't yet support CSP, in some cases, this header can create XSS vulnerabilities in otherwise safe websites.

If you do not need to support legacy browsers, it is recommended that you use Content-Security-Policy without allowing unsafe-inline scripts instead. Furthermore do not set this header or explicitly turn it off with: `X-XSS-Protection: 0` or `X-XSS-Protection: 1; mode=block`.

Python:

````Python
http_header = {  'X-XSS-Protection: 1; mode=block'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'X-XSS-Protection',
            value: '1; mode=block'
            }
        ]
    ]
````

## Set-Cookie

The Set-Cookie HTTP response header is used to send a cookie from the server to the user agent, so the user agent can send it back to the server later.

You should look at the following cheat sheet and determine what you want to implement from it:
[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#cookies)

Python:

````Python
http_header = {  'Set-Cookie: yummy_cookie=choco'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Set-Cookie',
            value: 'yummy_cookie=choco'
            }
        ]
    ]
````

## Access-Control-Allow-Origin

If you don't use this header, your site is protected by default by the Same Origin Policy (SOP). What this header does is relax this control in specified circumstances.

Set specific origins instead of *. Checkout [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) for details.  

Python:

````Python
http_header = {  'Access-Control-Allow-Origin: https://yoursite.com'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Access-Control-Allow-Origin',
            value: 'https://yoursite.com'
            }
        ]
    ]
````

## Cross-Origin-Opener-Policy (COOP)

The HTTP Cross-Origin-Opener-Policy (COOP) response header allows you to ensure a top-level document does not share a browsing context group with cross-origin documents.

It's Recommended to Isolate the browsing context exclusively to same-origin documents.

Python:

````Python
http_header = {  'HTTP Cross-Origin-Opener-Policy: same-origin'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'HTTP Cross-Origin-Opener-Policy',
            value: 'same-origin'
            }
        ]
    ]
````

## Cross-Origin-Embedder-Policy (COEP)

The HTTP Cross-Origin-Embedder-Policy (COEP) response header prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

Recommendation for this is a document can only load resources from the same origin, or resources explicitly marked as loadable from another origin.

Python:

````Python
http_header = {  'Cross-Origin-Embedder-Policy: require-corp'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Cross-Origin-Embedder-Policy',
            value: 'require-corp'
            }
        ]
    ]
````

## Cross-Origin-Resource-Policy (CORP)

The Cross-Origin-Resource-Policy (CORP) header allows you to control the set of origins that are empowered to include a resource.

You should limit current resource loading to the site and sub-domains only.

Python:

````Python
http_header = {'Cross-Origin-Resource-Policy: same-site'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Cross-Origin-Resource-Policy',
            value: 'same-site'
            }
        ]
    ]
````

## Server

The Server header describes the software used by the origin server that handled the request — that is, the server that generated the response.

Recommended is to remove this header or set non-informative values.
An example of non-informative values: `Server: webserver`. An example of an actual is `Server: Apache/2.4.1 (Unix)` this means that the server is running Apache version 2.4.1 on a Unix system.

Python:

````Python
http_header = {  'Server: webserver'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Server',
            value: 'webserver'
            }
        ]
    ]
````

## X-DNS-Prefetch-Control

The default behavior of browsers is to perform DNS caching which is good for most websites. But if you do not control links on your website, you might want to set off as a value to disable DNS prefetch to avoid leaking information to those domains.

Python:

````Python
http_header = {  'X-DNS-Prefetch-Control: off'}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'X-DNS-Prefetch-Control',
            value: 'off'
            }
        ]
    ]
````

## FLoC (Federated Learning of Cohorts)

FLoC is a method proposed by Google in 2021 to deliver interest-based advertisements to groups of users ("cohorts"). The Electronic Frontier Foundation, Mozilla, and others believe FLoC does not do enough to protect users' privacy.

It's depended on the maker itself if they want to include it or not. To disable it you can see the following code blocks.

If you want to partake into this you can check out the [blog from google](https://developers.google.com/privacy-sandbox/blog/floc).

Python:

````Python
http_header = {  'Permissions-Policy: interest-cohort=() '}

response = requests.get('example.com', headers=http_header)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
         source: '/*',
        headers: [
            {
            key: 'Permissions-Policy',
            value: 'interest-cohort=()'
            }
        ]
    ]
````

## Expect-CT

The Expect-CT header lets sites opt-in to reporting of Certificate Transparency (CT) requirements.

This header is not recommend to be used because it's deprecated. You can remove it but it's not necessary.

Python:

````Python
# Define the URL and data for the POST request
url = "https://example.com"
data = {"key1": "value1", "key2": "value2"}

# Prepare the request manually
s = requests.Session()
req = requests.Request('POST', url, data=data)
prepped = req.prepare()

# Remove the generated Expect-CT header
if 'Expect-CT' in prepped.headers:
    del prepped.headers['Expect-CT']

# Send the request
response = s.send(prepped)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)', // Match all paths
        headers: [
          {
            key: 'Expect-CT', // Specify the header key
            value: '', // Set an empty value to remove the header
          },
        ],
      },
    ];
  },
};
````

## X-Frame-Option

This sets if the browser should be allowed to render a pag in a `<frame>`,`<iframe>`,`<embed>` or `<object>`. This is useful to avoid clickjacking attacks, by ensuring that the websites content is not embedded into other sites.

Do not set use Content Security Policy (CSP) frame-ancestors directive. This obsoletes X-Frame-Options

## X-Powered-By, X-AspNet-Version, X-AspNetMvc-Version

These headers give information about their .Net version or which technologies are used.

The X-Powered-By header describes the technologies used by the webserver. This information exposes the server to attackers. Using the information in this header, attackers can find vulnerabilities easier.

You should remove all  headers.

Python:

````Python
# Define the URL and data for the POST request
url = "https://example.com"
data = {"key1": "value1", "key2": "value2"}

# Prepare the request manually
s = requests.Session()
req = requests.Request('POST', url, data=data)
prepped = req.prepare()

# Remove the generated Expect-CT header
if 'X-Powered-By' in prepped.headers:
    del prepped.headers['X-Powered-By']

# Send the request
response = s.send(prepped)
````

next.config.js:

````Javascript
module.exports = {
  poweredByHeader: false,
};
````

## Public-Key-Pins (HPKP)

This header is on the bottom because it actually should be removed

The HTTP Public-Key-Pins response header is used to associate a specific cryptographic public key with a certain web server to decrease the risk of MITM attacks with forged certificates.

This header should be removed.

````Python
# Define the URL and data for the POST request
url = "https://example.com"
data = {"key1": "value1", "key2": "value2"}

# Prepare the request manually
s = requests.Session()
req = requests.Request('POST', url, data=data)
prepped = req.prepare()

# Remove the generated Expect-CT header
if 'Public-Key-Pins' in prepped.headers:
    del prepped.headers['Public-Key-Pins']

# Send the request
response = s.send(prepped)
````

next.config.js:

````Javascript
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)', // Match all paths
        headers: [
          {
            key: 'Public-Key-Pins', // Specify the header key
            value: '', // Set an empty value to remove the header
          },
        ],
      },
    ];
  },
};
````
