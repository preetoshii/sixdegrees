import json

# Load the candidate words from the JSON file
with open('candidate_words.json', 'r') as f:
    words = json.load(f)

# The size of each batch
batch_size = 50

# Calculate the number of batches
num_batches = (len(words) + batch_size - 1) // batch_size

# Create and write to each batch file
for i in range(num_batches):
    start_index = i * batch_size
    end_index = start_index + batch_size
    batch_words = words[start_index:end_index]
    
    # Define the batch file name
    batch_filename = f'candidate_batches/batch_{i + 1}.json'
    
    # Write the batch to a new JSON file
    with open(batch_filename, 'w') as f:
        json.dump(batch_words, f, indent=2)

print(f"Successfully split {len(words)} words into {num_batches} batch files.") 