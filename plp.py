import random


def generate_love_letter(recipient_name, sender_name):
    opening = random.choice([
        f"My dearest {recipient_name},",
        f"My love {recipient_name},",
        f"To my darling {recipient_name},",
        f"To the love of my life, {recipient_name},"
    ])
    body = random.choice([
        "I wanted to take a moment to express my love for you. You bring so much happiness and joy into my life, and I am grateful for every moment we spend together. I love the way you laugh, your beautiful smile, and the way you make me feel. I love you more every day and I cannot imagine life without you.",
        "Every moment with you is a treasure. I cherish the time we spend together, and I am so grateful for your love. You are my best friend, my partner, and my soulmate. I love you deeply, completely, and forever. You make my life so much better, and I am thankful for you every day.",
        "I am writing this letter to let you know how much I love you. You are the most important person in my life, and I am grateful for you every day. Your love and support have been a constant source of comfort and happiness for me, and I cannot imagine life without you. I promise to always love you, support you, and cherish you, now and forever.",
        "I wanted to take a moment to express my love for you. You bring so much happiness and joy into my life, and I am grateful for every moment we spend together. I love the way you laugh, your beautiful smile, and the way you make me feel. I love you more every day and I cannot imagine life without you.",
        "Every moment with you is a treasure. I cherish the time we spend together, and I am so grateful for your love. You are my best friend, my partner, and my soulmate. I love you deeply, completely, and forever. You make my life so much better, and I am thankful for you every day.",
        "I'm so lucky to have you in my life. Happy Valentine's Day!",
        "You are my soulmate and my best friend. Happy Valentine's Day!",
        "Happy Valentine's Day to the one who makes me feel like a kid again.",
        "Happy Valentine's Day to the one who brings happiness to my life.",
        "Happy Valentine's Day to the one who brings happiness to my life.",
        "Happy Valentine's Day to the one who brings happiness to my life.",

        "I am writing this letter to let you know how much I love you. You are the most important person in my life, and I am grateful for you every day. Your love and support have been a constant source of comfort and happiness for me, and I cannot imagine life without you. I promise to always love you, support you, and cherish you, now and forever.",
        "You are my soulmate and my best friend. Happy Valentine's Day!",
        "Happy Valentine's Day to the one who makes me feel like a kid again.",
        "Happy Valentine's Day to the one who brings happiness to my life.",
        "Happy Valentine's Day to the one who brings happiness to my life.",
        "Happy Valentine's Day to the one who brings happiness to my life."
    ])
    closing = random.choice([
        f"Yours always and forever,\n{sender_name}",
        f"With all my love,\n{sender_name}",
        f"Forever and always,\n{sender_name}",
        f"Love always,\n{sender_name}"
    ])
    letter = f"{opening}\n\n{body}\n\n{closing}"
    return letter


def main():
    recipient_name = input("Enter the name of the recipient: ")
    sender_name = input("Enter your name: ")
    love_letter = generate_love_letter(recipient_name, sender_name)
    print(love_letter)


if __name__ == "__main__":
    main()
