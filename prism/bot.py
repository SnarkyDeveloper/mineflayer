from javascript import require
import asyncio
from .events import EventHandler, setup_events

mineflayer = require("mineflayer", "latest")

class Bot(EventHandler):
    def __init__(self, *, username=None, password=None, auth=None, version=None, offline=False, hide_errors=False, keep_alive=True, view_distance=10, client_id=None, access_token=None, session=None, keep_alive_interval=10000, keep_alive_timeout=30000, keep_alive_max_count=3, keep_alive_max_interval=30000, keep_alive_max_timeout=30000, keep_alive_max_missed=3, keep_alive_max_missed_interval=30000):
        """
        Bot class for controlling a Minecraft bot using mineflayer.
        
        Parameters:
        - username: The username of the bot.
        - password: The password of the bot.
        - auth: The authentication method.
        - version: The Minecraft version.
        - offline: Whether to use offline mode.
        - hide_errors: Whether to hide errors.
        - keep_alive: Whether to keep the bot alive.
        - view_distance: The view distance of the bot.
        - client_id: The client ID.
        - access_token: The access token.
        - session: The session.
        - keep_alive_interval: The keep alive interval.
        - keep_alive_timeout: The keep alive timeout.
        - keep_alive_max_count: The maximum count of keep alive.
        - keep_alive_max_interval: The maximum interval of keep alive.
        - keep_alive_max_timeout: The maximum timeout of keep alive.
        - keep_alive_max_missed: The maximum missed of keep alive.
        - keep_alive_max_missed_interval: The maximum missed interval of keep alive.
        
        Returns:
        - Bot: Needs to be started with `run` or `start` methods.
        """
        super().__init__()
        self.pending_events = []
        self.username = username
        self.password = password
        self.auth = auth
        self.version = version
        self.offline = offline
        self.hide_errors = hide_errors
        self.keep_alive = keep_alive
        self.view_distance = view_distance
        self.client_id = client_id
        self.access_token = access_token
        self.session = session
        self.keep_alive_interval = keep_alive_interval
        self.keep_alive_timeout = keep_alive_timeout
        self.keep_alive_max_count = keep_alive_max_count
        self.keep_alive_max_interval = keep_alive_max_interval
        self.keep_alive_max_timeout = keep_alive_max_timeout
        self.keep_alive_max_missed = keep_alive_max_missed
        self.keep_alive_max_missed_interval = keep_alive_max_missed_interval
        self.bot = None

    def event(self, func):
        """Decorator to store and register events."""
        event_name = func.__name__.replace("on_", "")
        self.pending_events.append((event_name, func))
        return func

    def register_event(self, event_name, handler):
        """Registers an event handler for a specific event."""
        if self.bot and hasattr(self.bot, 'on'):
            def wrapper(*args):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(handler(*args))
            self.bot.on(event_name, wrapper)

    async def start(self, host='localhost', port=25565):
        """
        Starts the bot asynchronously and connects to a Minecraft server.
        
        Parameters:
        - host: The host to connect to.
        - port: The port to connect to.
        Returns:
        - None
        """
        self.bot = mineflayer.createBot({
            'username': self.username,
            'password': self.password,
            'host': host,
            'port': port,
            'auth': self.auth,
            'version': self.version,
            'offline': self.offline,
            'hide_errors': self.hide_errors,
            'keep_alive': self.keep_alive,
            'view_distance': self.view_distance,
            'client_id': self.client_id,
            'access_token': self.access_token,
            'session': self.session,
            'keep_alive_interval': self.keep_alive_interval,
            'keep_alive_timeout': self.keep_alive_timeout,
            'keep_alive_max_count': self.keep_alive_max_count,
            'keep_alive_max_interval': self.keep_alive_max_interval,
            'keep_alive_max_timeout': self.keep_alive_max_timeout,
            'keep_alive_max_missed': self.keep_alive_max_missed,
            'keep_alive_max_missed_interval': self.keep_alive_max_missed_interval
        })

        # Register manually defined events
        for event_name, handler in self.pending_events:
            self.register_event(event_name, handler)

        await setup_events(self)
        try:
            await asyncio.Future()  # Keeps the coroutine running forever
        except asyncio.CancelledError:
            self.shutdown(reason="Cancelled")

    def shutdown(self, reason="Shutdown"):
        """Gracefully shuts down the bot."""
        if self.bot:
            print("\nShutting down bot...")
            try:
                # Add timeout handling for the end() call
                asyncio.wait_for(self.bot.end(reason), timeout=5.0)
            except Exception:
                # If end() times out or fails, force exit
                pass
            finally:
                self.bot = None

    def run(self, host='localhost', port=25565):
        """
        Synchronous entry point that properly integrates with an asyncio loop.
        Parameters:
        - host: The host to connect to.
        - port: The port to connect to.
        Returns:
        - None
        """
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.start(host, port))
        except KeyboardInterrupt:
            loop.run_until_complete(asyncio.sleep(0.1))
            self.shutdown(reason="KeyboardInterrupt")
        finally:
            loop.close()
