import os
import sys
from base64 import b64encode
from httpie.plugins import ConverterPlugin
from httpie.output.streams import BinarySuppressedError


class ImagePlugin(ConverterPlugin):

    def convert(self, content_bytes):
        if self.is_iterm2():
            data = b64encode(content_bytes).decode()
            sys.stdout.write('\033]1337;File=inline=1:{}\a\n'.format(data))
            return 'image/*', ''
        raise BinarySuppressedError()

    @classmethod
    def supports(cls, mime):
        if mime.startswith('image/') and cls.is_iterm2():
            return True
        return False

    @classmethod
    def is_iterm2(cls):
        return os.environ.get('TERM_PROGRAM') == 'iTerm.app'
