from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="#",
    color=(255, 255, 255),
    name="player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

venus_flytrap = Actor(
    char="V",
    color=(51, 255, 119),
    name="VenusFlytrap",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=19, base_defense=3, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=80),
)

demon = Actor(
    char="D",
    color=(77, 0, 0),
    name="Demon",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=3, base_power=20),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=150),
)

skeleton = Actor(
    char="s",
    color=(77, 0, 0),
    name="Skeleton",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=20, base_defense=3, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

grimm_reaper = Actor(
    char="R",
    color=(6, 0, 13),
    name="Grimm Reaper",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=8, base_power=20),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

tornado_kitty = Item(
    char="&",
    color=(0,106,128),
    name="Tornado Kitty",
    consumable=consumable.TornadoKittyDamageConsumable(damage=11, radius=3),
)

large_health_potion = Item(
    char="!",
    color=(102,204,255),
    name="Large Health Potion",
    consumable=consumable.HealingConsumable(amount=15),
)

medium_health_potion = Item(
    char="!",
    color=(230,251,255),
    name="Medium Health Potion",
    consumable=consumable.HealingConsumable(amount=10),
)

small_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Small Health Potion",
    consumable=consumable.HealingConsumable(amount=6),
)
void_scroll = Item(
    char="~",
    color=(255,25,102),
    name="Void Scroll",
    consumable=consumable.VoidDamageConsumable(damage=20000, radius=4),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 131, 255), name="WoodenDagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 91, 255), name="Sword", equippable=equippable.Sword())

boofy_sword = Item(char="/", color=(0, 77, 0), name="Boofy Sword", equippable=equippable.BoofySword())

demon_sword = Item(char="/", color=(26, 0, 0), name="Demon Sword", equippable=equippable.DemonSword())


leather_armor = Item(
    char="[",
    color=(133, 89, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

boofy_armor = Item(
    char="[", color=(51, 0, 77), name="Boofy Armor", equippable=equippable.BoofyArmor()
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)

demon_armor = Item(
    char="[", color=(179, 0, 30), name="Demon Armor", equippable=equippable.DemonArmor()
)