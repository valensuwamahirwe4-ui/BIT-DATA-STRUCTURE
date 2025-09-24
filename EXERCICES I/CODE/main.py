from array import array

servings = [3, 5, 2, 4, 6, 3, 5]

total_servings = sum(servings)
average_servings = total_servings / len(servings)
min_servings = min(servings)
max_servings = max(servings)

report = (
    f"\n📊 Nutrition Survey Report\n"
    f"---------------------------\n"
    f"Total Fruit Servings: {total_servings}\n"
    f"Average Servings per Participant: {average_servings:.2f}\n"
    f"Minimum Servings: {min_servings}, Maximum Servings: {max_servings}\n"
)
print(report)

threshold = 4
status = "Above Standard" if average_servings > threshold and max_servings > threshold else "Below Standard"
print(f"✅ Survey Status: {status}\n")

food_items = ["Banana", "Apple", "Carrot", "Dates"]
print("📋 Food Items Before:", food_items)

food_items.append("Eggplant")

food_items = [item for item in food_items if not item.startswith("C")]

food_items.sort()
print("📋 Food Items After:", food_items, "\n")

servings_array = array('i', servings[:5])
array_sum = sum(servings_array)
list_sum = sum(servings)
print(f"📦 Array Sum: {array_sum}, List Sum: {list_sum}\n")

records = [
    {"id": 1, "name": "Alice", "value": 3},
    {"id": 2, "name": "Bob", "value": 5},
    {"id": 3, "name": "Charlie", "value": 2}
]

for record in records:
    if record["name"] == "Bob":
        record["value"] = 6

records = [record for record in records if record["name"] != "Charlie"]

total_value = sum(record["value"] for record in records)
print("🗂️ Updated Records:", records)
print(f"🧮 Total Value from Records: {total_value}")
