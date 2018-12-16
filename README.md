# My Website
http://www.vincela.com/

## Powered by Pelican
My website is generated via Pelican, a static site generator written in Python.

Building: `make.bat`

### Notes

If there's an error trying to parse Markdown, then run:

```
pip install markdown
```

## CSS
My website is laid out according to hand-crafted CSS which you can find [under /themes/vince-theme/](https://github.com/vincentlaucsb/vincela.com/tree/master/themes/vince-theme/static/css-raw). The CSS is itself generated from SCSS stylesheets.

For those of you not in the know, SCSS is a superset of CSS which makes it a lot more tolerable to build stylesheets.

## Nginx Config

```
server {
    listen 80;
    server_name [IP ADDRESS] vincela.com;
    
    location / {
        root [PATH TO]/vincela.com/output;
        autoindex on;
    }

    
}
```
