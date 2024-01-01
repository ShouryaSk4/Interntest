import pymongo

# Replace 'your_uri_here' with your actual MongoDB URI
mongodb_uri = 'mongodb+srv://intern:JeUDstYbGTSczN4r@interntest.i7decv0.mongodb.net/'
database_name = 'intern'  # Replace with your actual database name
collection_name = 'papers'  # Replace with your actual collection name

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_uri)
database = client[database_name]
collection = database[collection_name]

# Retrieve data from MongoDB
documents = collection.find({}, {"transcription": 1, "title": 1})

# Write data to a text file
output_file_path = 'output.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for document in documents:
        transcription = document.get('transcription', '')
        title = document.get('title', '')

        # Write the combination of transcription and title to the file
        output_file.write(f"Title: {title}\nTranscription: {transcription}\n\n")

print(f"Data written to {output_file_path}")

# Close the MongoDB connection
client.close()
