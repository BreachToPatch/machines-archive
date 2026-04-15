# Apache 2.4.49 — vulnerable to CVE-2021-41773 (Path Traversal + RCE via mod_cgi)
# This image intentionally uses a vulnerable version for CTF training purposes.
FROM httpd:2.4.49

# Copy our custom configuration that enables the vulnerability
COPY httpd.conf /usr/local/apache2/conf/httpd.conf

# Create a simple index page
RUN echo "<html><body><h1>Welcome to Bee-Path</h1></body></html>" \
    > /usr/local/apache2/htdocs/index.html

# Ensure the cgi-bin directory exists
RUN mkdir -p /usr/local/apache2/cgi-bin

EXPOSE 80
