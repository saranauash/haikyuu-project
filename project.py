import math
import json
import os

def check_access(func):
    def wrapper(self, current_user_role, *args, **kwargs):
        if isinstance(current_user_role, str) and current_user_role.lower() == "admin":
            result = func(self, current_user_role, *args, **kwargs)
            with open("admin_log.txt", "a", encoding="utf-8") as log:
                log.write(f"Action: {func.__name__} by admin\n")
            return result
        else:
            print(f"❌ ACCESS DENIED: {current_user_role}")
            return None
    return wrapper

class Player:
    def __init__(self, name, age, power, stamina):
        self.name = name
        self.age = age
        self.power = power
        self.stamina = stamina

    def get_info(self):
        return f"{self.name} (P: {self.power}, S: {self.stamina})"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "power": self.power,
            "stamina": self.stamina,
            "role": type(self).__name__
        }

class Setter(Player):
    def __init__(self, name, age, power, stamina, intelligence):
        super().__init__(name, age, power, stamina)
        self.intelligence = intelligence

    def special_skill(self):
        return f"🏐 {self.name}: Tactical Toss ({self.intelligence})"

class Spiker(Player):
    def __init__(self, name, age, power, stamina, jump_height):
        super().__init__(name, age, power, stamina)
        self.jump_height = jump_height

    def special_skill(self):
        return f"🔥 {self.name}: Power Spike ({self.jump_height}cm)"

class Libero(Player):
    def __init__(self, name, age, power, stamina, defense_rate):
        super().__init__(name, age, power, stamina)
        self.defense_rate = defense_rate

    def special_skill(self):
        return f"🛡️ {self.name}: Rolling Receive ({self.defense_rate})"

class TeamManager:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = {} 

    @check_access
    def add_player(self, current_user_role, number, player_obj):
        self.players[number] = player_obj
        print(f"✅ Added #{number}")

    @check_access
    def remove_player(self, current_user_role, number):
        if number in self.players:
            self.players.pop(number)
            print(f"🗑️ Removed #{number}")

    def find_player(self, number):
        return self.players.get(number)

    def calculate_efficiency_index(self):
        if not self.players: return 0
        total = sum(math.sqrt(p.power * p.stamina) for p in self.players.values())
        return round(total / len(self.players), 2)

    @check_access
    def save_to_json(self, current_user_role, filename="team_data.json"):
        data = {str(k): v.to_dict() for k, v in self.players.items()}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Saved to {filename}")

    def export_report(self, filename="social_structure.txt"):
        idx = self.calculate_efficiency_index()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Team: {self.team_name}\nEfficiency: {idx}\n")
            for n, p in self.players.items():
                f.write(f"#{n} {p.get_info()}\n")
        print(f"📄 Exported to {filename}")

if __name__ == "__main__":
    karasuno = TeamManager("Karasuno High")
    karasuno.add_player("admin", 9, Setter("Kageyama", 16, 90, 85, 95))
    karasuno.add_player("admin", 10, Spiker("Hinata", 16, 85, 100, 120))
    
    print(f"Efficiency: {karasuno.calculate_efficiency_index()}")
    karasuno.save_to_json("admin")
    karasuno.export_report()