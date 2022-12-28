import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

log = logging.getLogger(__name__)
ignore_empty = plugins.toolkit.get_validator('ignore_empty')

DEFAULT_VIDEO_FORMATS = 'mp4 ogg webm'

class VideoviewerPlugin(plugins.SingletonPlugin):

    '''This plugin makes views of video resources, using an <video> tag'''

    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)

    # IResourceView

    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'theme/templates')
        self.formats = config.get(
            'ckan.preview.video_formats',
            DEFAULT_VIDEO_FORMATS).split()

    def info(self):
        return {'name': 'videoviewer',
                'title': plugins.toolkit._('Video'),
                'icon': 'video-camera',
                'schema': {'video_url': [ignore_empty, str]},
                'iframed': False,
                'always_available': False,
                'default_title': plugins.toolkit._('Video'),
                }

    def can_view(self, data_dict):
        return (data_dict['resource'].get('format', '').lower()
                in self.formats)

    def view_template(self, context, data_dict):
        return 'video_view.html'

    def form_template(self, context, data_dict):
        return 'video_form.html'