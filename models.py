from dataclasses import dataclass, field


@dataclass
class CommandInfo:
    name: str
    description: str = ""
    aliases: list[str] = field(default_factory=list)
    usage: str = ""
    admin_only: bool = False
    custom_prefix: str | None = None  # None 表示使用全局唤醒前缀，"" 表示无前缀


@dataclass
class PluginInfo:
    name: str
    display_name: str = ""
    description: str = ""
    commands: list[CommandInfo] = field(default_factory=list)
    icon_url: str = ""  # base64 data URI 或空
    order: int = 99

    def __post_init__(self):
        if not self.display_name:
            self.display_name = self.name
