class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = int(mana_cost)
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills = "\n"
        if self.skills:
            for skill, mana in self.skills.items():
                skills += f"==={skill} - {mana}\n"
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}" + skills


