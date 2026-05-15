import math
import json
import os

def check_access(func):
    def wrapper(self, current_user_role, *args, **kwargs):
        if isinstance(current_user_role, str) and current_user_role.lower() == "admin":
            result = func(self, current_user_role, *args, **kwargs)
            try:
                with open("admin_log.txt", "a", encoding="utf-8") as log:
                    log.write(f"Action: {func.__name__} performed by admin\n")
            except IOError:
                pass
            return result
        else:
            print(f"❌ ACCESS DENIED: Role '{current_user_role}' is not authorized.")
            return None
    return wrapper

class Player:
    def __init__(self, name, age, power, stamina):
        self.name = name
        self.age = age
        self.power = power
        self.stamina = stamina

    def get_info(self):
        return f"{self.name} (Age: {self.age}, Power: {self.power}, Stamina: {self.stamina})"

    def to_dict(self):
        """Converts object data to a dictionary for JSON storage"""
        return {
            "name": self.name, "age": self.age,
            "power": self.power, "stamina": self.stamina,
            "role": type(self).__name__
        }
    
class Setter(Player):
    def __init__(self, name, age, power, stamina, intelligence):
        super().__init__(name, age, power, stamina)
        self.intelligence = intelligence

    def special_skill(self):
        return f"🏐 {self.name}: Tactical Toss (Intel: {self.intelligence})"

class Spiker(Player):
    def __init__(self, name, age, power, stamina, jump_height):
        super().__init__(name, age, power, stamina)
        self.jump_height = jump_height

    def special_skill(self):
        return f"🔥 {self.name}: Power Spike (Jump: {self.jump_height}cm)"

class Libero(Player):
    def __init__(self, name, age, power, stamina, defense_rate):
        super().__init__(name, age, power, stamina)
        self.defense_rate = defense_rate

    def special_skill(self):
        return f"🛡️ {self.name}: Rolling Receive (Def: {self.defense_rate})"

class TeamManager:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = {} 

    @check_access
    def add_player(self, current_user_role, number, player_obj):
        self.players[number] = player_obj
        print(f"✅ Player #{number} added to {self.team_name}.")

    @check_access
    def remove_player(self, current_user_role, number):
        if number in self.players:
            del self.players[number]
            print(f"🗑️ Player #{number} removed.")
        else:
            print(f"⚠️ Player #{number} not found.")

    def calculate_efficiency_index(self):
        """Complex calculation using math module"""
        if not self.players: return 0
        total = sum(math.sqrt(p.power * p.stamina) for p in self.players.values())
        return round(total / len(self.players), 2)

    @check_access
    def save_data(self, current_user_role, filename="team_data.json"):
        """File I/O: Saving to JSON"""
        try:
            data = {str(k): v.to_dict() for k, v in self.players.items()}
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print(f"💾 Data successfully saved to {filename}")
        except Exception as e:
            print(f"❌ Error during JSON export: {e}")

    def export_report(self, filename="social_structure.txt"):
        """File I/O: Professional Text Report"""
        try:
            idx = self.calculate_efficiency_index()
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"=== {self.team_name.upper()} FINAL EVALUATION ===\n")
                f.write(f"Team Efficiency Index: {idx}\n")
                f.write("-" * 40 + "\n")
                for n, p in self.players.items():
                    f.write(f"Number: {n} | {p.get_info()} | Skill: {p.special_skill()}\n")
            print(f"📄 Professional report exported to {filename}")
        except Exception as e:
            print(f"❌ Error during report export: {e}")

if __name__ == "__main__":
    print(f"--- Haikyuu Management System Initialized ---")
    karasuno = TeamManager("Karasuno High")
    
    karasuno.add_player("admin", 9, Setter("Kageyama Tobio", 16, 90, 85, 95))
    karasuno.add_player("admin", 10, Spiker("Hinata Shoyo", 16, 85, 100, 120))
    karasuno.add_player("admin", 4, Libero("Nishinoya Yuu", 17, 70, 90, 98))

    print(f"\nFinal Team Efficiency: {karasuno.calculate_efficiency_index()}")
    karasuno.save_data("admin")
    karasuno.export_report()
    print("--- Process Completed ---")