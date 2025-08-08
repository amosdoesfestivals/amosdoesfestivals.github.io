# BayesWatch.github.io
Group homepage

## Adding a Blog post

add a markdown file to the `_posts` folder above with the name:

`<YYYY>-<MM>-<DD>-<SHORT_TITLE>.md`.

The contents of the file should be:

```
---
layout: post
title: <YOUR TITLE>
author: <FIRSTNAME> <SECONDNAME>
---
<CONTENTS>
```

## Crossposting

Add a `linkto:<URL>` to the above, and omit <CONTENTS>.


## Adding a publication

Append `_data/publications.yml`

## Updating the rota

Modify lines 4, 5 and 11 in `generate_rota_names.py`, and run script. Copy and paste output into `_data/rota_names.yml` (or modify this file directly) to update the rota.

## Development tips

To view your changes before submission, install jekyll and serve the website locally one
way to do this is using conda:

```bash
conda create -n jekyll
conda activate jekyll
conda install -c conda-forge rb-jekyll
jekyll serve --trace
```

Now you can navigate to <http://localhost:4000> to view the site and make edits.
