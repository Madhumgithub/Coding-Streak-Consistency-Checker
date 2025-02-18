
### **🐍 script.py**
```python
import datetime

try:
    with open("streak.txt", "r") as file:
        streak = int(file.read().strip())
except FileNotFoundError:
    streak = 0

coded_today = input("Did you code today? (yes/no): ").lower()

if coded_today == "yes":
    streak += 1
    print(f"🔥 Streak: {streak} days!")
else:
    streak = 0
    print("❌ Streak lost!")

with open("streak.txt", "w") as file:
    file.write(str(streak))
