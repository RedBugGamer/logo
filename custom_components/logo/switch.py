from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from . import DOMAIN, CONF_ID, CONF_CONTROLLER_ID, _LOGGER

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CONTROLLER_ID): cv.string
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up logo switch from YAML."""
    controller_id = config[CONF_CONTROLLER_ID]
    controller = hass.data[DOMAIN].get(controller_id)
    
    if controller is None:
        raise ValueError(f"Controller ID '{controller_id}' not found.")
    _LOGGER.debug("Controller is",controller)
    # switch = LogoSwitch(controller)
    # async_add_entities([switch])

class LogoSwitch(SwitchEntity):

    def __init__(self, controller, name="Logo Switch", output_address="Q0.0"):
        self._controller = controller
        self._name = name
        self._output_address = output_address
        self._is_on = False

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._is_on

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        # Send ON command to controller
        await self._controller.set_output(self._output_address, True)
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        # Send OFF command to controller
        await self._controller.set_output(self._output_address, False)
        self._is_on = False
        self.async_write_ha_state()

    async def async_update(self):
        """Fetch the current state from the controller."""
        self._is_on = await self._controller.get_output_state(self._output_address)