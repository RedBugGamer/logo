import logging
from homeassistant import core
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from .const import (
    DOMAIN,
    CONF_ID,
    CONF_TSAP,
    CONF_IP_ADDRESS,
    CONF_CONTROLLER_ID
)

_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_IP_ADDRESS): cv.string,
        vol.Required(CONF_TSAP): vol.Coerce(float),
        vol.Required(CONF_ID): cv.string,
    })
}, extra=vol.ALLOW_EXTRA)


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Logo interface component."""
    controller_config = config[DOMAIN]
    controller_id = controller_config[CONF_ID]
    hass.data.setdefault(DOMAIN, {})[controller_id] = controller_config
    return True
