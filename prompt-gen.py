topics = [
    "Thinking, Fast and Slow",
    "Man's Search for Meaning",
    "Quiet: The Power of Introverts in a World That Can't Stop Talking",
    "The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma",
    "Influence: The Psychology of Persuasion",
    "The Man Who Mistook His Wife for a Hat and Other Clinical Tales",
    "Blink: The Power of Thinking Without Thinking",
    "The Power of Habit: Why We Do What We Do in Life and Business",
    "Flow: The Psychology of Optimal Experience",
    "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
    "Predictably Irrational: The Hidden Forces That Shape Our Decisions",
    "Outliers: The Story of Success",
"How to Win Friends & Influence People",
"Emotional Intelligence: Why It Can Matter More Than IQ",
"Mindset: The New Psychology of Success",
"The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good Life",
"The Interpretation of Dreams",
"12 Rules for Life: An Antidote to Chaos",
"The Tipping Point: How Little Things Can Make a Big Difference",
"Maybe You Should Talk to Someone: A Therapist, Her Therapist, and Our Lives Revealed",
"The Psychopath Test: A Journey Through the Madness Industry",
"Man and His Symbols",
"The 48 Laws of Power",
"The Righteous Mind: Why Good People are Divided by Politics and Religion",
"Talking to Strangers: What We Should Know About the People We Don't Know",
"Games People Play",
"The Lucifer Effect: Understanding How Good People Turn Evil",
"Adult Children of Emotionally Immature Parents",
"The Psychology of Money",
"Behave: The Biology of Humans at Our Best and Worst",
"Memories, Dreams, Reflections",
"The Art of Loving",
"Attached: The New Science of Adult Attachment and How It Can Help You Find—and Keep—Love",
"Drive: The Surprising Truth About What Motivates Us",
"Stumbling on Happiness",
"An Unquiet Mind: A Memoir of Moods and Madness",
"The Happiness Hypothesis: Finding Modern Truth in Ancient Wisdom",
"Daring Greatly",
"Grit: The Power of Passion and Perseverance",
"The Courage to Be Disliked",
"On Becoming a Person: A Therapist's View of Psychotherapy",
"Civilization and Its Discontents",
"Why We Sleep: Unlocking the Power of Sleep and Dreams",
"The Gifts of Imperfection",
"Nudge: Improving Decisions About Health, Wealth, and Happiness",
"The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change",
"Love's Executioner and Other Tales of Psychotherapy",
"What Happened to You?: Conversations on Trauma, Resilience, and Healing",
"Modern Man in Search of a Soul",
"How to Change Your Mind: The New Science of Psychedelics"
]
prompts = [
    You are a book insights AI. Your task is to extract psychological wellbeing insights from the given book—focusing on emotional clarity, behavior change, self-awareness, resilience, motivation, meaning, relationships, and stress reduction.

Input: <BOOK_NAME>

Output strictly in this JSON format (no explanation, no markdown, no extra text):

{
  "book_name": "<BOOK_NAME>",
  "psychological_wellbeing_key_points": [
    {
      "insight_name": "Short title of the insight",
      "insight_text": "A deep, clear 5–8 sentence explanation describing why this insight matters for psychological wellbeing and one practical micro-action to apply it."
    }
  ]
}

Rules:
- Include at least 5 insights.
- Do not include any fields other than: book_name, insight_name, insight_text.
- Output only valid JSON.
]

prompt_suffix = ". The options for each Question are: Strongly Agree, Agree, Neutral, Disagree and Strongly Disagree. The Options have a weight 2 ,4 ,6 ,8, 10 or 10 , 8, 6, 4,2. Where 10 Represents that there is higher prevalence of the symptom. Think Step By Step for the scores. The Questions should be a 50-50% mix of 2 ,4 ,6 ,8, 10 or 10 , 8, 6, 4,2. But 10 Should always imply the symptoms worse because of the condition. I want the Output in a csv format. Give only output. Columns Are: Condition Name, Question Text, Strongly Agree Score, Agree Score, Neutral Score, Disagree Score, Strongly Disagree Score"

from datetime import datetime
import csv

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_txt = f"prompts_{timestamp}.txt"
output_csv = f"prompts_{timestamp}.csv"

# Open TXT file and write output
with open(output_txt, 'w', encoding='utf-8') as f:
    for prompt in prompts:
        for topic in topics:
            f.write(prompt + topic + prompt_suffix + "~\n")

# Open CSV file and write output
with open(output_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Prompt', 'Topic', 'Full Prompt'])  # Header
    for prompt in prompts:
        for topic in topics:
            writer.writerow([prompt, topic, prompt + topic + prompt_suffix + "~"])

print(f"Output saved to {output_txt} and {output_csv}")