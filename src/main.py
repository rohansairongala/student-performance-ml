import pandas as pd

def calculate_average(scores):
    valid_scores = []
    for score in scores:
        if isinstance(score, (int, float)):
            valid_scores.append(score)
        else:
            try:
                # Convert strings to float if possible
                score = float(score)
                valid_scores.append(score)
            except (ValueError, TypeError):
                print(f"Ignoring invalid score: {score}")
    if len(valid_scores) == 0:
        return None
    return sum(valid_scores) / len(valid_scores)

def main():
    print("Student Performance ML Project Initialized\n")
    
    # Load CSV
    df = pd.read_csv("data/scores.csv")  # path from src folder
    print("Loaded student scores:\n", df, "\n")
    
    # Calculate averages
    averages = {}
    for index, row in df.iterrows():
        name = row['Name']
        scores = row[1:].tolist()  # all subjects
        avg = calculate_average(scores)
        averages[name] = avg
    
    # Print results
    print("Student averages:")
    for name, avg in averages.items():
        if avg is not None:
            print(f"{name}: {avg:.2f}")
        else:
            print(f"{name}: No valid scores")
    
    # Save averages to CSV
    avg_df = pd.DataFrame(list(averages.items()), columns=['Name', 'Average'])
    avg_df.to_csv("data/averages.csv", index=False)
    print("\nAverages saved to data/averages.csv")

if __name__ == "__main__":
    main()