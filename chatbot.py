import re
import response as resp
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        # Convert user message and recognized words to lowercase
        user_message_lower = [word.lower() for word in message]
        recognized_words_lower = [word.lower() for word in list_of_words]
        highest_prob_list[bot_response] = message_probability(user_message_lower, recognized_words_lower, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hieeee','hiii'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'coding'], required_words=['coding'])
    response('Nothing much just improving my skills and learning from my friends to improve my ablities', ['whats', 'up'], required_words=['whats'])
    response('You are not a failure. You are still learning and growing.',['failure'],required_words=['failure'])
    
    # long responses
    response(resp.ADVICE, ['give', 'advice'], required_words=['advice'])
    response(resp.EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(resp.HAPPY,['why','happy'],required_words=['happy'])
    response(resp.END,['without','me','end'],required_words=['end'])
    response(resp.LIFE,['do','anything','life','living'],required_words=['anything','life'])
    response(resp.SAD,['embarrassed','bad','shitty','sucks','sad'],single_response=True)
    response(resp.STRESS,['stress','terrified','anxious','nervous','scared','stressed'],single_response=True)
    response(resp.LIFE,['what','life'],single_response=True)
    response(resp.LIVE,['why','live'],single_response=True)
    response(resp.LOVE,['nobody','love','loves'],single_response=True)
    response(resp.HOPE,['hope','hopelessness',],single_response=True)
    response(resp.FIT,['fit','world','good enough'],single_response=True)
    response(resp.CRAZY,['crazy','going'],required_words=['crazy'])
    response(resp.BETTER,['better','mood','negative'],single_response=True)
    response(resp.ME,['why','me'],single_response=True)
    response(resp.TIRED,['tired','felling'],single_response=True)


    #new response
    response(resp.Snap,['snap','wrong'],single_response=True)
    response(resp.Exhausted,['exhausted'],single_response=True)
    response(resp.Enjoy,['enjoy','anymore'],single_response=True)
    response(resp.Concentrate,['conentrate','focus'],single_response=True)
    response(resp.Burden,['burden','everyone'],single_response=True)
    response(resp.Wearing_a_mask,['mask','waering'],single_response=True)
    response(resp.feeling,['feeling','not happy','never','better'],single_response=True)




    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return resp.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    if user_input is not None:
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        print("User Input:", split_message)  # Add this line for debugging
        response = check_all_messages(split_message)
        print("Bot Response:", response)  # Add this line for debugging
        return response
    else:
        return ""




# Define a route for the homepage that renders the HTML file
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the chatbot API that takes in user input and returns a response
@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    if request.method == 'POST':
        user_input = str(request.form.get('user_input'))
        response = get_response(user_input)
        return jsonify({'response': response})
    else:
        return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    print("Welcome to (chatbot name) ")
    app.debug = True
    app.run()
