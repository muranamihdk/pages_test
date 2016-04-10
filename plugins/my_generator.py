import logging
from itertools import chain

from pelican import signals
from pelican.contents import Page, is_valid_content
from pelican.utils import process_translations
from pelican.generators import PagesGenerator


logger = logging.getLogger(__name__)


class MyPagesGenerator(PagesGenerator):
    """Generate my pages
    - Modify settings' key
            self.settings['PAGE_PATHS'],
            self.settings['PAGE_EXCLUDES']):
            self.settings['PAGE_ORDER_BY'])
    - Add page.template attribute
            page.template = 'my_page'
    - Delete signals
            signals.page_generator_init.send(self)
            signals.page_generator_finalized.send(self)
            signals.page_writer_finalized.send(self, writer=writer)
    """

    def __init__(self, *args, **kwargs):
        self.pages = []
        self.hidden_pages = []
        self.hidden_translations = []
        super(MyPagesGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        all_pages = []
        hidden_pages = []
        for f in self.get_files(
                self.settings['MY_PAGE_PATHS'],
                exclude=self.settings['MY_PAGE_EXCLUDES']):
            page = self.get_cached_data(f, None)
            if page is None:
                try:
                    page = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Page,
                        context=self.context,
                        preread_signal=signals.page_generator_preread,
                        preread_sender=self,
                        context_signal=signals.page_generator_context,
                        context_sender=self)
                    page.template = 'my_page'
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)
                    continue

                if not is_valid_content(page, f):
                    self._add_failed_source_path(f)
                    continue

                if page.status.lower() == "published":
                    all_pages.append(page)
                elif page.status.lower() == "hidden":
                    hidden_pages.append(page)
                else:
                    logger.error(
                        "Unknown status '%s' for file %s, skipping it.",
                        page.status, f)
                    self._add_failed_source_path(f)
                    continue

                self.cache_data(f, page)

            self.add_source_path(page)

        self.pages, self.translations = process_translations(
            all_pages,
            order_by=self.settings['MY_PAGE_ORDER_BY'])
        self.hidden_pages, self.hidden_translations = \
            process_translations(hidden_pages)

        self._update_context(('pages', 'hidden_pages'))

        self.save_cache()
        self.readers.save_cache()

    def generate_output(self, writer):
        for page in chain(self.translations, self.pages,
                          self.hidden_translations, self.hidden_pages):
            writer.write_file(
                page.save_as, self.get_template(page.template),
                self.context, page=page,
                relative_urls=self.settings['RELATIVE_URLS'],
                override_output=hasattr(page, 'override_save_as'))


def get_generators(generators):
    return [MyPagesGenerator]

def register():
    signals.get_generators.connect(get_generators)
