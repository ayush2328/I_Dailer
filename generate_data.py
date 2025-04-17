import random
import csv
from pathlib import Path

def generate_number(country_code, is_spam=False):
    if is_spam:
        patterns = ['999', '000', '123', '888']
        base = random.choice(patterns)
        num_body = (base * 4)[:10]  # repeat & trim
    else:
        digits = [str(random.randint(0, 9)) for _ in range(10)]
        num_body = ''.join(digits)
    return f"+{country_code}{num_body}"

def generate_dataset(num_samples=1000, spam_ratio=0.4):
    countries = ['1', '44', '91', '61', '81']
    data = []

    spam_count = int(num_samples * spam_ratio)
    not_spam_count = num_samples - spam_count

    for _ in range(spam_count):
        number = generate_number(random.choice(countries), is_spam=True)
        data.append((number, 'spam'))

    for _ in range(not_spam_count):
        number = generate_number(random.choice(countries), is_spam=False)
        data.append((number, 'not_spam'))

    random.shuffle(data)
    return data

def save_to_csv(data, filename='synthetic_number_data.csv'):
    path = Path(__file__).parent / filename
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['number', 'label'])
        writer.writerows(data)
    print(f"✅ File saved at: {path.resolve()}")

if __name__ == "__main__":
    print("📦 Creating dataset...")
    dataset = generate_dataset(1000, spam_ratio=0.4)
    save_to_csv(dataset)


