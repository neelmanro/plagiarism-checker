# Imports
from flask import Flask, render_template,request


app = Flask(__name__)

# Common Grammer Words
grammar_words = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
    "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from",
    "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself", "him",
    "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just",
    "me", "more", "most", "my", "myself", "no", "nor", "not", "now", "of", "off", "on", "once",
    "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
    "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them",
    "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too",
    "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which",
    "while", "who", "whom", "why", "with", "would", "you", "your", "yours", "yourself",
    "yourselves"
}



# Home page
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        try:
            essay_one = request.form["essay_one"]
            essay_two = request.form["essay_two"]

            cleaned_one = essay_one.replace(",", " ").replace(".", " ").replace(";", " ").lower().split()
            cleaned_two = essay_two.replace(",", " ").replace(".", " ").replace(";", " ").lower().split()

            set_one = {word for word in cleaned_one if word not in grammar_words}
            set_two = {word for word in cleaned_two if word not in grammar_words}

            common = set_one & set_two
            uncommon = set_one - set_two

            total = len(set_one)
            common_length = len(common)
            uncommon_length = len(uncommon)

            similarity_score = (common_length / total) * 100 if total > 0 else 0

            if similarity_score > 75:
                similarity = "High Similarity"
            elif 40 < similarity_score <= 75:
                similarity = "Medium Similarity"
            else:
                similarity = "Low Similarity"

            return render_template("home.html",
                                   uncommon=uncommon,
                                   common=common,
                                   uncommon_length=uncommon_length,
                                   common_length=common_length,
                                   similarity_score=round(similarity_score, 2),
                                   similarity=similarity)

        except Exception as e:
            return f"Something went wrong: {str(e)}", 500

    return render_template("home.html")
        
        
    
    





if __name__ == "__main__":
    app.run(debug=True)


