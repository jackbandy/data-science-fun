# Agent Guidelines

Notes on how automated agents should behave in this repo.

## Rate limiting

When downloading batches of files from external hosts (Wikimedia Commons, etc.), space requests out with a `sleep 2` between each `curl` call. Wikimedia's CDN enforces a 429 rate limit on burst downloads; hitting it returns a 2.2KB HTML error page instead of the image. Always verify downloads are valid images (`file` command) before proceeding.

Use thumbnail URLs via the Wikimedia Commons API when downloading from Wikimedia:
```
https://commons.wikimedia.org/w/api.php?action=query&titles=File:NAME.jpg&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json
```
This returns the `/thumb/` URL, which is served from different cache nodes than full-resolution files and is less likely to be rate-limited.
