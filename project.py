import math
import json
import os

def check_access(func):
    def wrapper(self, current_user_role, *args, **kwargs):
        if isinstance(current_user_role, str) and current_user_role.lower() == "admin":
            return func(self, current_user_role, *args, **kwargs)
        else:
            print(f"❌ ACCESS DENIED for role '{current_user_role}': Only 'admin' can perform this action.")
            return None
    return wrapper

class Player:
    def __init__(self, name, age, power, stamina):
        self.name = name
        self.age = age
        self.power = power
        self.stamina = stamina

    def get_info(self):
        return f"{self.name} (Power: {self.power}, Stamina: {self.stamina})"

class Setter(Player):
    def __init__(self, name, age, power, stamina, intelligence):
        super().__init__(name, age, power, stamina)
        self.intelligence = intelligence

    def special_skill(self):
        return f"🏐 {self.name} uses 'Tactical Toss' (Intel: {self.intelligence})"

class Spiker(Player):
    def __init__(self, name, age, power, stamina, jump_height):
        super().__init__(name, age, power, stamina)
        self.jump_height = jump_height

    def special_skill(self):
        return f"🔥 {self.name} uses 'Power Spike' (Jump: {self.jump_height}cm)"

class Libero(Player):
    def __init__(self, name, age, power, stamina, defense_rate):
        super().__init__(name, age, power, stamina)
        self.defense_rate = defense_rate

    def special_skill(self):
        return f"🛡️ {self.name} uses 'Rolling Receive' (Defense: {self.defense_rate})"

class TeamManager:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = {} 

    @check_access
    def add_player(self, current_user_role, number, player_obj):
        """Добавление игрока в систему (Week 1-2)"""
        self.players[number] = player_obj
        print(f"✅ Player {player_obj.name} added to {self.team_name} at number {number}.")

    
    @check_access
    def remove_player(self, current_user_role, number):
        """Удаление игрока из системы (Week 2)"""
        if number in self.players:
            removed_player = self.players.pop(number)
            print(f"🗑️ Player {removed_player.name} removed from number {number}.")
        else:
            print(f"⚠️ Player with number {number} not found.")

    def find_player(self, number):
        """Поиск игрока по номеру (Week 2)"""
        player = self.players.get(number)
        if player:
            print(f"🔍 Found: {player.get_info()}")
            return player
        else:
            print(f"⚠️ No player found at number {number}.")
            return None

    
    def calculate_team_stats(self):
        """Расчет средней силы команды (Week 3)"""
        if not self.players:
            return 0
        total_power = sum(p.power for p in self.players.values())
        avg_power = total_power / len(self.players)
        return math.ceil(avg_power)

    def export_report(self, filename="social_structure.txt"):
        """Экспорт отчета в файл (Week 4)"""
        avg_p = self.calculate_team_stats()
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"--- TEAM REPORT: {self.team_name} ---\n")
                f.write(f"Average Team Power: {avg_p}\n")
                f.write("Roster:\n")
                for num, p in self.players.items():
                    f.write(f"#{num} {p.get_info()} - Role: {type(p).__name__}\n")
            print(f"📄 Report exported to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    karasuno = TeamManager("Karasuno High")

    kageyama = Setter("Kageyama Tobio", 16, 90, 85, 95)
    hinata = Spiker("Hinata Shoyo", 16, 85, 100, 120)
    nishinoya = Libero("Nishinoya Yuu", 17, 70, 90, 98)

    print("--- Week 1 & 2: Testing Management System ---")
    
    karasuno.add_player("admin", 9, kageyama) 
    karasuno.add_player("admin", 10, hinata)
    karasuno.add_player("admin", 4, nishinoya)

    karasuno.find_player(10)
    
    karasuno.remove_player("admin", 4)
    
    karasuno.add_player("guest", 1, Player("Test User", 20, 50, 50)) 

    print("\n--- Final Team Status ---")
    print(f"Average Team Power: {karasuno.calculate_team_stats()}")
    
    for p in karasuno.players.values():
        if hasattr(p, 'special_skill'):
            print(p.special_skill())

    karasuno.export_report()