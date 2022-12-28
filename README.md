# ckanext-videoviewer

## Requirements

NOTE: Supporting only CKAN 2.9.7 with Python 3.X.

## Installation

To install ckanext-videoviewer:

1. Activate your CKAN virtual environment, for example:

```
. /usr/lib/ckan/default/bin/activate
```

2. Clone the source and install it on the virtualenv

```
git clone https://github.com/espresso3389/ckanext-videoviewer.git
cd ckanext-videoviewer
pip install -e .
pip install -r requirements.txt
```

3. Add `videoviewer` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).

4. [OPTIONAL] If you want to enable preview for video files by default, add `videoviewer` to the `ckan.views.default_views` setting on the CKAN config file also.

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

```
sudo service apache2 reload
```

## Config settings

`ckan.preview.video_formats` to specify supporting video file extensions. The default is `mp4 ogg webm`.

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
