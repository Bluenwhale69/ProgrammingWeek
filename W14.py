class Unit:
    def __init__(self, name, hp):
        self.name = name  
        self.hp = hp      

    def move(self):
        return f"{self.name} walks forward."

    def get_status(self):
        return f"Name: {self.name} | HP: {self.hp}"


class Hero(Unit):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana 

    def move(self):
        return f"{self.name} dashes quickly!"

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts Fireball! (Mana left: {self.mana})"
        return f"{self.name} has not enough mana!"


def main():
    unit1 = Unit("Goblin", 50)
    unit2 = Unit("Orc", 80)
    hero1 = Hero("Arthur", 100, 50)
    hero2 = Hero("Lancelot", 120, 20)

    grid_board = [
        [unit1, hero1],
        [hero2, unit2]
    ]

    print("=== Board Status & OOP Actions ===")
    
    row = 0
    while row < len(grid_board):
        col = 0
        while col < len(grid_board[row]):
            character = grid_board[row][col]
            
            print(f"Position [{row}][{col}]:")
            print("  Status:", character.get_status())
            print("  Action:", character.move())
            
            if isinstance(character, Hero):
                print("  Special:", character.cast_spell())
                
            print("-" * 30)
            col += 1
        row += 1

    print("=== Testing Error Handling ===")
    
    try:
        invalid_position = grid_board[5][5]
    except IndexError:
        print("Error: พยายามเข้าถึงตำแหน่งอาร์เรย์ที่ไม่มีอยู่จริง (IndexError)")
    except Exception as e:
        print(f"พบข้อผิดพลาดอื่นๆ: {e}")


if __name__ == "__main__":
    main()