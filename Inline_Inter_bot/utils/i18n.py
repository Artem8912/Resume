from fluent_compiler.bundle import FluentBundle

from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        locales_map={
            "ru": ("ru", "en","fr"),
            "en": ("en", "ru","fr"),
            "fr": ("fr","ru","en")
        },translators=
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["locales/ru/LC_MESSAGES/txt.ftl"])),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["locales/en/LC_MESSAGES/txt.ftl"]))
        ,
        FluentTranslator(
            locale='fr',
            translator=FluentBundle.from_files(
                locale='fr-FR',
                filenames=["locales/fr/LC_MESSAGES/txt.ftl"]
            )
        )
        ]
        ,root_locale='en'
    )
    return translator_hub