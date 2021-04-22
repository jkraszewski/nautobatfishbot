"""Plugin declaration for nautobatfishbot."""

__version__ = "0.1.0"

from nautobot.extras.plugins import PluginConfig


class NautobatfishbotConfig(PluginConfig):
    """Plugin configuration for the nautobatfishbot plugin."""

    name = "nautobatfishbot"
    verbose_name = "Nautobatfishbot"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobatfishbot."
    base_url = "nautobatfishbot"
    required_settings = []
    min_version = "1.0.0-beta.4"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobatfishbotConfig  # pylint:disable=invalid-name
