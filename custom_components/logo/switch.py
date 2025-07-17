from homeassistant.components.switch import PLATFORM_SCHEMA
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from . import DOMAIN, CONF_ID, CONF_CONTROLLER_ID

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CONTROLLER_ID): cv.string
})