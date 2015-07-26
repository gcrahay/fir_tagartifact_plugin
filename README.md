# Tags as artifacts for FIR - Fast Incident Response

[FIR](https://github.com/certsocietegenerale/FIR) (Fast Incident Response by [CERT Société générale](https://cert.societegenerale.com/)) is an cybersecurity incident management platform designed with agility and speed in mind. It allows for easy creation, tracking, and reporting of cybersecurity incidents.

# Features

This plugin adds a new artifact type in FIR. These artifacts are typed tags that classify your events.

# Install

Follow the generic plugin installation instructions in [the FIR wiki](https://github.com/certsocietegenerale/FIR/wiki/Plugins).
Make sure the following line is included in the `urlpatterns` variable in `fir/urls.py`:

```
url(r'^tagartifact/', include('fir_tagartifact.urls', namespace='tagartifact')),
```

Then, migrate the database structure:

```bash
(your_env)${FIR_HOME}$ ./manage.py migrate
```
