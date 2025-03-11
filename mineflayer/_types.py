bot = None
class ChatMessage: # chat message stuff (for typehints)
    def __init__(self, username, message, timestamp):
        global bot
        self.bot = bot
        self.author = None
        self.message = message

class Item: # item stuff (for typehints)
    def __init__(self, item):
        self.id = item.id
        self.name = item.name
        self.displayName = item.displayName
        self.count = item.count
        self.maxCount = item.maxCount
        self.stackable = item.stackable
        self.maxStackSize = item.maxStackSize
        self.maxDamage = item.maxDamage
        self.damage = item.damage
        self.maxDurability = item.maxDurability
        self.durability = item.durability
        self.maxStackSize = item.maxStackSize
        # finish later
class Entity: # entity stuff (for typehints)
    def __init__(self, entity):
        self.id = entity.id
        self.type = entity.type
        self.username = entity.username
        self.mobType = entity.mobType
        self.displayName = entity.displayName
        self.entityType = entity.entityType
        self.kind = entity.kind
        self.objectType = entity.objectType
        self.count = entity.count
        self.position = entity.position
        self.velocity = entity.velocity
        self.yaw = entity.yaw
        self.pitch = entity.pitch
        self.height = entity.height
        self.width = entity.width
        self.onGround = entity.onGround
        self.equipment = entity.equipment
        self.heldItem = entity.heldItem
        self.metadata = entity.metadata
        self.noClip = entity.noClip
        self.vehicle = entity.vehicle
        self.passenger = entity.passenger
        self.health = entity.health
        self.food = entity.food
        self.elytraFlying = entity.elytraFlying
        self.player = entity.player
        self._entity = entity
        
    def getCustomName(self) -> ChatMessage:
        return self._entity.getCustomName()

    def getDroppedItem(self) -> Item:
        return self._entity.getDroppedItem()