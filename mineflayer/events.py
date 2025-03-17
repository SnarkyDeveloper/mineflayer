import inspect
import logging

logger = logging.getLogger(__name__)
class EventHandler:
    def __init__(self):
        self._events = {}
    def register_event(self, event_name: str, callback):
        """Registers a callback function to an event."""
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(callback)

    async def dispatch(self, event_name: str, *args, **kwargs):
        """Dispatches an event, calling all registered callbacks."""
        if event_name in self._events:
            for callback in self._events[event_name]:
                if callable(callback):
                    await callback(*args, **kwargs)

    def event(self, event_name=None):
        """Decorator to manually register event handlers."""
        def decorator(func):
            nonlocal event_name
            if event_name is None: # If no event name is provided, use the function name
                event_name = func.__name__.replace("on_", "") 

            self.register_event(event_name, func)
            return func
        return decorator

# Create event handler instance
events = EventHandler()

# Define event handlers
async def on_spawn(*args):
    await events.dispatch("spawn", *args)

async def on_chat(*args):
    _, *remaining_args = args 
    await events.dispatch("chat", *remaining_args)
async def on_error(*args):
    logger.error(f"Error: {args}")
    await events.dispatch("error", *args)
async def setup_events(bot):
    """Register events after bot is created"""
    bot._bot.on("spawn", on_spawn)
    bot._bot.on("chat", on_chat)
    bot._bot.on("error", on_error)