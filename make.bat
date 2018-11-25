start sass --watch ./themes/vince-theme/static/scss:./output/theme/css --style compressed

start pelican -r content

cd output
start python -m pelican.server